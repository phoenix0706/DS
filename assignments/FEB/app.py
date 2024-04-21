from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login')
def login():
    return 'Login Page'

@app.route('/user/<username>')
def profile(username):
    return f'User {username}'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))












































'''

ANS 2

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

if __name__ == '__main__':
    app.run()
    '''



'''
ANS 3

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    return """
    <h1>Company Name: ABC Corporation</h1>
    <p>Location: India</p>
    <p>Contact Detail: 999-999-9999</p>
    """

if __name__ == '__main__':
    app.run()

'''

