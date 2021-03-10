from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# Using difficulty select screen as home page
@views.route('/', methods=['POST', 'GET'])
def difficulty_select():
    return render_template("difficulty_select.html")

@views.route('/category')
def category_select():
    return render_template("category.html")

@views.route('/game_start')
def game_start():
    return render_template("answer.html")