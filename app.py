
import os
from flask import Flask
# import tkinter as tk

app = Flask(__name__)

FLASK_DEBUG = 1
# FLASK_APP = app.py

@app.route("/")
def print_hello():
    print("Hello from the app, its working !")
    return "<h1>Hello from the app, its working !</hi>"

#
# def print_hello():
#     # Use a breakpoint in the code line below to debug your script.
#     return   # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == "__main__":
    print_hello()
    app.run(host="https://tic-tac-toe-tic-tac-toe.192.168.99.103.nip.io/")
