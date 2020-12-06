from flask import Flask, redirect, url_for
import tkinter as tk

app = Flask(__name__)

@app.route('/')
def go_to_app():
    return redirect(url_for('http://tic-tac-toe-tic-tac-toe.192.168.99.103.nip.io'))

#
# def print_hello():
#     # Use a breakpoint in the code line below to debug your script.
#     return "Hello from the app"  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    # print_hello()
    app.run()
