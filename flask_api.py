# Import
import time
import uuid
from flask import Flask
from celery import Celery
from pymongo import MongoClient
from flask_restplus import Api, Resource, fields

# Define required variables
APP_SECRET_KEY = "AsyncTaskScheduling-FMT"
CELERY_BROKER_URL = "redis://localhost:6379/0"
# Temp. account was used and already destroyed. Do not forget to alter! 
MONGO_CLIENT_URL = "mongodb+srv://async_admin:async_admin@aws-mongodb-cluster0.y6ldx.mongodb.net/AsyncTaskScheduling?retryWrites=true&w=majority"

# Setting up Flask, REST-API, Celery
app = Flask(__name__)
api = Api(app, version="0.1", title="AsyncTaskScheduling-FMT", description="AsyncTaskScheduling-FMT")
celery_client = Celery(app.name, broker=CELERY_BROKER_URL)

# Connect MongoDB Atlas
db_client = MongoClient(MONGO_CLIENT_URL)
db = db_client["AsyncTaskScheduling"] # Database
calculations_collection = db["calculations"] # Colletion/Table

# Define namespaces for REST-API
calculationsEP = api.namespace("calculationsEP", description="Operations for Calculations")
calculationEP = api.namespace("calculationEP", description="Operations for Single Calculation")

# Define api models for calculations
calculations_model = api.model("calculations", 
        {
            "pid": fields.Integer(description="PID", example="73694a4c-e790-4015-b97c-ebaad83280f2", readonly=True),
            "name": fields.String(description="Full name", example="Someone Else", required=True),
            "height": fields.Integer(description="Height", example=170, required=True),
            "weight": fields.Integer(description="Weight", example=55),
        }
    )

# Asyn - Time-consuming task via Celery
@celery_client.task
def bmi_calculation(data):
    """Returns the body-mass index for given values and 
    here, it mimics the time-consuming function

    Args:
        data (dict): Contains following keys `pid`, `name`, `height`, `weight`. 
    """
    time.sleep(30) # To make it more realistic
    pid, name, weight, height = data["pid"], data["name"], data["weight"], data["height"]
    data["bmi"] = int(weight) / ((int(height) / 100) ** 2)
    calculations_collection.insert_one(data)

# calculations Collection Part
@calculationsEP.route("/")
@calculationsEP.response(200, "Successful operation!")
@calculationsEP.response(500, "Internal error somewhere in the code")
class calculationsEP(Resource):
    def get(self):
        calculations_list = []
        query_result = calculations_collection.find({}, {'_id': False})
        for result in query_result:
            calculations_list.append(result)
        return calculations_list

    @calculationsEP.expect(calculations_model, validate=True)
    def post(self):
        data = api.payload
        data["pid"] = str(uuid.uuid4())
        bmi_calculation.apply_async(args=[data])
        return f"Your work is submitted with an PID of {data['pid']}"

# Individual calculation operation
@calculationEP.route("/<string:pid>")
@calculationEP.response(200, "Success")
@calculationEP.response(500, "Internal error somewhere in the code")
class calculationByPID(Resource):
    @calculationEP.doc(params={"pid":"ID number of the calculation"})
    def get(self, pid):
        finding_list = []
        query_result = calculations_collection.find({'pid': pid}, {'_id': False})
        for result in query_result:
            finding_list.append(result)
        if len(finding_list) > 0:
            return finding_list
        else:
            return f"No such calculation with ID of {pid}"

    @calculationEP.doc(params={"pid":"ID number of the calculation"})
    def delete(self, pid):
        calculations_collection.delete_one({"pid": pid})
        return f"The entry with ID {pid} will be deleted"

# Run
if __name__ == "__main__":
    app.secret_key = APP_SECRET_KEY
    app.run(debug=True)