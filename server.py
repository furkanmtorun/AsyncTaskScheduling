# Import
from flask import Flask, render_template, url_for, redirect, flash, request
from pymongo import MongoClient
from celery import Celery
import time
import uuid

# Define
SECRET_KEY = 'somePrettyAwesomeSecretKeyHere'
CELERY_BROKER_URL = 'redis://localhost:6379/0'

# Connect MongoDB
db_client = MongoClient("mongodb+srv://admin:admin@aws-mongodb-cluster0.y6ldx.mongodb.net/async_pipeline?retryWrites=true&w=majority")
db = db_client["async_pipeline"] # Database
users_collection = db ["users"] # Colletion/Table

# Setting up Flask and Celery
app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
client = Celery(app.name, broker=CELERY_BROKER_URL)

# Create index page
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else: 
        data = {}
        data["pid"] = str(uuid.uuid4())
        data["name"] = request.form['name']
        data["height"] = request.form['height']
        data["weight"] = request.form['weight']
        bmi_calculation.apply_async(args=[data])
        flash(f"Calculation is on the way! Keep this PID: {data['pid']}")
        return redirect(url_for('index'))

# # Create query page
@app.route("/list", methods=["GET", "POST"])
def list():
    list_result = {}
    list_result["n_document"] = users_collection.count_documents({})
    list_result["documents"] = users_collection.find({})
    return render_template("list.html", list_result=list_result)

@client.task
def bmi_calculation(data):
    time.sleep(60) # To make it more realistic
    pid, name, weight, height = data["pid"], data["name"], data["weight"], data["height"]
    data["bmi"] = int(weight) / ( (int(height)/100) ** 2 )
    users_collection.insert_one(data)

# Run flask
if __name__ == "__main__":
    app.run(debug=True)