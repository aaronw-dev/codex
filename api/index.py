from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os
app = Flask(__name__)
app.url_map.strict_slashes = False

creds_dict = json.loads(os.environ.get(
    ("FIREBASE_SERVICE_ACCOUNT_CREDENTIAL")))
cred = credentials.Certificate(creds_dict)

firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client()


def getHeader():
    with open("api/header.html", "r")as file:
        return file.read()


@app.route('/')
def home():
    print(os.listdir("api"))
    return render_template("index.html", header=getHeader())


@app.route('/onboarding')
def onboarding():
    return render_template("onboarding.html", header=getHeader())


@app.route('/app')
def renderApp():

    return render_template("app.html", header=getHeader())


@app.route('/courses/<course>/<index>')
def lesson(course, index):
    course_ref = db.collection("courses").document(course)
    course_info = course_ref.get().to_dict()
    collection_array = []
    for doc in course_ref.collection(f"lesson-{index}").get():
        collection_array.append(doc.to_dict())
    course_info["lessons"] = collection_array
    print(course_info)
    return course_info


@app.route('/courses/')
def courses():
    courses = []
    for doc in db.collection("courses").get():
        courses.append(doc.to_dict())
    return {"lessons": courses}
