# Import
from flask import Flask
from flask_restplus import Api, Resource, fields
from pymongo import MongoClient
from celery import Celery
import time
import uuid

# Define
APP_SECRET_KEY = "AsyncTaskScheduling-FMT"
CELERY_BROKER_URL = "redis://localhost:6379/0"

# Setting up Flask, REST-API, Celery
app = Flask(__name__)
api = Api(app, version="0.1", title="AsyncTaskScheduling-FMT", description="AsyncTaskScheduling-FMT")
celery_client = Celery(app.name, broker=CELERY_BROKER_URL)

# Connect MongoDB Atlas | Temporary account was used, so it is already destroyed :)
db_client = MongoClient("mongodb+srv://async_admin:async_admin@aws-mongodb-cluster0.y6ldx.mongodb.net/AsyncTaskScheduling?retryWrites=true&w=majority")
db = db_client["AsyncTaskScheduling"] # Database
users_collection = db["users"] # Colletion/Table

# Define namespaces for REST-API
usersCollection = api.namespace("Users Operation Collection", description="Operations for Users")
processCollection = api.namespace("Process Operation Collection", description="Operations for Process Details")

# Define api models for users
users_model = api.model("users", 
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
    time.sleep(30) # To make it more realistic
    pid, name, weight, height = data["pid"], data["name"], data["weight"], data["height"]
    data["bmi"] = int(weight) / ( (int(height)/100) ** 2 )
    users_collection.insert_one(data)

# Users Collection Part
@usersCollection.route("/")
@usersCollection.response(200, "Successful operation!")
@usersCollection.response(500, "Internal error somewhere in the code")
class usersCollection(Resource):
    def get(self):
        users_list = []
        query_result = users_collection.find({}, {'_id': False})
        for result in query_result:
            users_list.append(result)
        return users_list

    @usersCollection.expect(users_model, validate=True)
    def post(self):
        data = api.payload
        data["pid"] = str(uuid.uuid4())
        bmi_calculation.apply_async(args=[data])
        return f"Your work is submitted with an PID of {data['pid']}"

# Individual process operation
@processCollection.route("/<string:pid>")
@processCollection.response(200, "Success")
@processCollection.response(500, "Internal error somewhere in the code")
class processByPID(Resource):
    @processCollection.doc(params={"pid":"ID number of the process"})
    def get(self, pid):
        finding_list = []
        query_result = users_collection.find({'pid': pid}, {'_id': False})
        for result in query_result:
            finding_list.append(result)
        if len(finding_list) > 0:
            return finding_list
        else:
            return f"No such process with ID of {pid}"

    @processCollection.doc(params={"pid":"ID number of the process"})
    def delete(self, pid):
        users_collection.delete_one({"pid": pid})
        return f"The entry with ID {pid} will be deleted"

# Run
if __name__ == "__main__":
    app.secret_key = APP_SECRET_KEY
    app.run(debug=True)