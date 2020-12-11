import os
from flask import Flask, render_template
from tkinter import *
from tkinter import messagebox

# the logic of Tic Tac Toe ------------------------------------------------

game_window = Tk()
game_window.title("TIC - TAC - TOE")


game_window.mainloop()






app = Flask(__name__)

FLASK_DEBUG = 1

@app.route("/")
def print_hello():
    print("Hello from the app, its working !")
    return render_template("index.html")

if __name__ == "__main__":
    # print_hello()
    app.run(host="0.0.0.0", port=8080)
