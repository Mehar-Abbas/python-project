import os
from flask import Flask, render_template
# import tkinter as tk

app = Flask(__name__)

FLASK_DEBUG = 1
# FLASK_APP = app.py

@app.route("/")
def print_hello():
    print("Hello from the app, its working !")
    return render_template("index.html")

if __name__ == "__main__":
    # print_hello()
    app.run(host="0.0.0.0", port=8080)
