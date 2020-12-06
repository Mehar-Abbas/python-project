
import os
from flask import Flask, redirect, url_for
# import tkinter as tk

FLASK_DEBUG = 1

app = Flask(__name__)

@app.route("/https://192.168.99.103:8443")
def print_hello():
    return "Hello from the app, its working !"
    # return redirect(url_for('/'))

#
# def print_hello():
#     # Use a breakpoint in the code line below to debug your script.
#     return   # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == "__main__":
    # print_hello()
    app.run()
