
import os
from flask import Flask, redirect, url_for
# import tkinter as tk

app = Flask(__name__)

@app.route("/")
def print_hello():
    return "Hello from the app, its working !"
    # return redirect(url_for('/'))

#
# def print_hello():
#     # Use a breakpoint in the code line below to debug your script.
#     return   # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == "__main__":
    # print_hello()
    app.run(host="https://192.168.99.103:8443/console", port=8443)
