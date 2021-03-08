from website import create_app
from flask import Flask, render_template, request, url_for, Response
from app import Game

app = create_app()

difficulty_mode = 0
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
      return f'hello. difficulty mode is {difficulty_mode}'
    else:
      return render_template("difficulty_select.html")

@app.route('/dynamic_difficulty/')
def dynamic_difficulty():
  difficulty_mode = 1
  return f"Flask: Call Difficulty({difficulty_mode})"

@app.route('/dance_difficulty/')
def dance_difficulty():
  difficulty_mode = 2
  return f"Flask: Call Difficulty({difficulty_mode})"

@app.route('/custom_difficulty/')
def custom_difficulty():
  difficulty_mode = 3
  return f"Flask: Call Difficulty({difficulty_mode})"

if __name__ == "__main__":
  app.run(host="127.0.0.1", port = 8080, debug=True)