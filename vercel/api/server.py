import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, render_template, send_file, redirect, request

app = Flask(__name__)
app.url_map.strict_slashes = False

# Use a service account.
cred = credentials.Certificate('creds/firebase.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


@app.route("/")
def home():
    return "skibidi"
