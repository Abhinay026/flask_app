from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/test_function")
def test_func():
    a = 7*9
    return "My number is {}".format(a)

@app.route("/input_url")
def request_input():
    data = request.args.get("x")
    return "My name is {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
