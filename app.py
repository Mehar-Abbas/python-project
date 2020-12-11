import os
from flask import Flask, render_template
from tkinter import *


# the logic of Tic Tac Toe ------------------------------------------------

app = Flask(__name__)

FLASK_DEBUG = 1

@app.route("/")
def print_hello():
    print("Hello from the app, its working !")
    return render_template("index.html")

if __name__ == "__main__":
    # print_hello()
    app.run()
