# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    user = ""
    computer = ""

    if request.method == "POST":
        user = request.form["choice"]
        computer = random.choice(choices)

        if user == computer:
            result = "🤝 It's a Tie!"
        elif (
            (user == "rock" and computer == "scissors") or
            (user == "paper" and computer == "rock") or
            (user == "scissors" and computer == "paper")
        ):
            result = "🎉 You Win!"
        else:
            result = "💻 Computer Wins!"

    return render_template("index.html", result=result, user=user, computer=computer)

if __name__ == "__main__":
    app.run(debug=True)