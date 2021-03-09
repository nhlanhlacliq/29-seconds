from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# Using difficulty select screen as home page
@views.route('/')
def difficulty_select():
    return render_template("new_diff.html")

@views.route('/category')
def category_select():
    return 'CateGory'

@views.route('/game_start')
def game_start():
    return 'Game Start'