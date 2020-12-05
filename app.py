from flask import Flask
import tkinter as tk

app = Flask(__name__)

@app.route('/')

def print_hello():
    # Use a breakpoint in the code line below to debug your script.
    return "Hello from the app"  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hello()
    app.run()