from flask import Flask
import tkinter as tk


app = Flask(__name__)

@app.route('/https://tic-tac-toe-tic-tac-toe.192.168.99.103.nip.io')

def print_hello():
    return "Hello from the app"

if __name__ == "__main__":
    print_hello()
    app.run()
