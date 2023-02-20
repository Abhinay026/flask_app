from flask import Flask

app = Flask(__name__)


@app.route("/Welcome")
def welcome():
    return "Welcome to ARM corporation"

@app.route("/")
def Company_details():
    return "Company Name: ABC Corporation<br>Location: India<br>Contact Detail: 999-999-9999"

if __name__=="__main__":
    app.run(host="0.0.0.0")