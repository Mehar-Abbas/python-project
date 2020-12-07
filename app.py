
import os
from flask import Flask, redirect, url_for
# import tkinter as tk

app = Flask(__name__)

FLASK_DEBUG = 1
# FLASK_APP = app.py

@app.route("/")
def print_hello():
    # print("Hello from the app, its working !")
    return "Hello from the app, its working !"

#
# def print_hello():
#     # Use a breakpoint in the code line below to debug your script.
#     return   # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == "__main__":
    # print_hello()
    app.run(debug=True)
