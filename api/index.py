from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
creds_dict = {
    "type": "service_account",
    "project_id": os.environ['project_id'],
    "private_key_id": os.environ['private_key_id'],
    "private_key": os.environ['private_key'],
    "client_email": os.environ['client_email'],
    "client_id": os.environ['client_id'],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ['client_x509_cert_url'],
    "universe_domain": "googleapis.com"
}
cred = credentials.Certificate(creds_dict)
app = firebase_admin.initialize_app(cred)

db = firestore.client()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return 'About'
