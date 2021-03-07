from flask import Flask, render_template, Response
from app import Game

app = Flask(__name__)

@app.route("/")
def index():
    # return "Good evening"
    
    # game = Game()
    # game.run()
    
    # Render HTML with count variable
    return render_template("index.html")


if __name__ == "__main__":
  app.run(host="127.0.0.1", port = 8080, debug=True)