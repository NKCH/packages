
from src import app
from flask import render_template


@app.route('/login', methods=['GET'])
def login():
    data = {
        "title": "login page",
        "body": "Login page rendering"
    }
    return render_template('signup.html', data=data)
