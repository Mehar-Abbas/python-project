
import os
from flask import Flask, redirect, url_for
# import tkinter as tk

FLASK_DEBUG = 1

app = Flask(__name__)

@app.route("/")
def print_hello():
    print("Hello from the app, its working !")
    return redirect(url_for('/http://tic-tac-toe-tic-tac-toe.192.168.99.103.nip.io/'))

#
# def print_hello():
#     # Use a breakpoint in the code line below to debug your script.
#     return   # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == "__main__":
    # print_hello()
    app.run()
