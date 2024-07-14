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


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return 'About'
