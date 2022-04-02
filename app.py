from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Proof of concept by Vipul Sahu"
