from flask import Flask

app = Flask(__name__)

@app.route("/")  # then the URL is: http://127.0.0.1:5002/ (the final slash)
def hello_world():
    return "<p>Hello world</p>"  # HTML code

