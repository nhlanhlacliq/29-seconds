from website import create_app
from flask import Flask, render_template, request, url_for, Response


app = create_app()



@app.route('/difficulty-mode/<int:difficulty_mode>')
def dynamic_difficulty(difficulty_mode):
  return f"Flask: Call Difficulty({difficulty_mode})"

if __name__ == "__main__":
  app.run(host="127.0.0.1", port = 8080, debug=True)