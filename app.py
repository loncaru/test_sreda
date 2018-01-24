from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

@app.route("/")
def index():
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Comments</title>
    </head>

    <body>
        <h1>Welcome!</h1>
    </body>

    </html>
    """
    return page

@app.route("/")
def comments():

    comments = {}
    for n in COMMENTS:
        comments[n.text] = n.date
    return render_template(comments = comments)