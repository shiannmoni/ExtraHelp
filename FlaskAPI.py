
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/vegan")

@app.route('/')
def index():
    return "hello"


@app.route('/register')
def new_user():
    return "Hi Newbie!"

@app.route('/login')
def user():
    return "welcome back!"

if __name__== '__main__':
    app.run(debug=True)

