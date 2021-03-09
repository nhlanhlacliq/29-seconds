from website import create_app
from website.difficulty import Difficulty as diff
from flask import Flask, render_template, request, url_for, Response


app = create_app()


@app.route('/difficulty-mode/<int:difficulty_mode>')
def difficulty_mode(difficulty_mode):
    # dm = Difficulty mode
    dm = diff(difficulty_mode)
    level = dm.get_difficulty()
    time = dm.get_time_limit()
    
    return f"Difficulty level: {level}. \nTime limit: {time}"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port = 8080, debug=True)