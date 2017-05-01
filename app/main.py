from flask import Flask, send_file

app = Flask(__name__)
@app.route("/")
def welcome():
    return send_file('./static/welcome.html')