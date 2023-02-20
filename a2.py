from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/user/<username>')
def user_profile(username):
    return f'User profile: {username}'

with app.test_request_context():
    print(url_for('index')) 
    print(url_for('user_profile', username='Abhinay'))