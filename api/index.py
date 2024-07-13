from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
app.url_map.strict_slashes = False

cred = credentials.Certificate('creds/firebase.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


@app.route('/')
def home():
    return render_template("index.html")
    # return 'Hello, World! This is the Vercel server for the <a href="https://awdev.codes">awdev.codes</a> website. Gimme a few days, then this thing will be up and running.'


@app.route('/about')
def about():
    return 'About'
