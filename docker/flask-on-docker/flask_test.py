from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

app.run(host="0.0.0.0")
