from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to my Flash Cards application"

@app.route('/date')
def date():
    return f"This page was served at {(str(datetime.now()))[:-7]}."

# Add a page that shows how many times it has been viewed
page_views = 0

@app.route('/views')
def views():
    global page_views
    page_views += 1
    return f"This page has been viewed {page_views} times"
