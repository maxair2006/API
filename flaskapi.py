from flask import Flask 

app = Flask(__name__)

@app.route("/")

def first_flask():
    return "hello welcome to flask program"
@app.route("/flask_2")

def second_flask():
    return"python is fun"
app.run()