"""
Install Flask:
Create a virtual environment
$ mkdir project 
$ cd project 
$ python -m venv venv
$ source venv/bin/activate

(venv) $ which pip
../project/venv/bin/pip
(venv) $ which python
../project/venv/bin/python

(venv) $ pip install --upgrade pip
(venv) $ pip install Flask

Run App:
To run the application, use the "flask" command or "python -m flask". 
You need to tell the Flask where your application is with the --app option. (filename.py)
As a shortcut, if the file is named app.py or wsgi.py, you don't have to use --app. 
To enable debug mode, use the --debug option:

$ python -m flask --app helloapp run --debug
 * Serving Flask app 'helloworld'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

Now head over to http://127.0.0.1:5000/, and you should see your hello world greeting!


Static Files
Dynamic web applications also need static files. That's usually where the CSS and JavaScript files are coming from. 
Just create a folder called static in your package or next to your module and it will be available at /static on the application.
http://127.0.0.1:5000/static/hello.js
url_for('static', filename='hello.js')

Rendering Templates
Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. 
Because of that Flask configures the Jinja2 template engine for you automatically.
Templates can be used to generate any type of text file. 
For web applications, you'll primarily be generating HTML pages, but you can also generate markdown, plain text for emails, any anything else.


About Responses
The return value from a view function is automatically converted into a response object for you. 
If the return value is a string it's converted into a response object with the string as response body, a 200 OK status code and a text/html mimetype. 
If the return value is a dict or list, jsonify() is called to produce a response. 
If you want to get hold of the resulting response object inside the view you can use the make_response() function.

API with JSON

"""
import os
import sys
sys.path.append("../basics")  # add sibling directory to the system path
from sqlite_basics import get_departments

from flask import Flask, redirect, render_template, request, session, url_for
from markupsafe import escape
from dotenv import load_dotenv


app = Flask(__name__)

# The secret keys should be stored external to the source code, so that they are not commit to revision control.
# set the SECRET_KEY configuration variable using an environment variable:
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# To set the environment variable, you can use the export command in your terminal or command prompt:
#       $ export SECRET_KEY='your_secret_key_here'

# You can also set environment variables using a .env file in your project directory. (add to .git)
# You can use a package like "python-dotenv" to load the variables from the file into your Flask application.
# Load environment variables from .env file on the same directory as this script:
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


app.config["DEBUG"] = True

# Modern web applications use meaningful URLs to help users. 
# Use the route() decorator to bind a function to a URL.
@app.route("/")                     # # http://127.0.0.1:5000/
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    
    return 'Hello, there!\nYou are not logged in.' # The default content type is HTML

# <username> in the route captures a value from the URL and passes it to the view function
@app.route('/user/<username>')      # http://127.0.0.1:5000/user/potter
def show_user_profile(username):
    # When returning HTML (the default response type in Flask), 
    # any user-provided values rendered in the output must be escaped to protect from injection attacks.
    return f"User Profile: {escape(username)}"

@app.route('/post/<int:postID>')   # http://127.0.0.1:5000/post/1
def show_post(postID):
    # show the post with the given id, the id is an integer
    return f'Post {postID}'

@app.route('/parameter')   # http://127.0.0.1:5000/parameter?id=333
def show_parameter():
    # To access parameters submitted in the URL (?key=value) you can use the The Request Object's args attribute:
    id = request.args.get('id', type=int)   # None if parameter is missing or type is not int.
    # show the post with the given id, the id is an integer
    return f"Parameter {id=}"

# APIs with JSON
@app.route("/userprofile")       # http://127.0.0.1:5000/userprofile
def get_user_profile():               
    user = get_user()

    # If you return a dict or list from a view, it will be converted to a JSON response.
    # return {
    #     "username": user.username,
    #     "house": user.house,
    #     # Generate the URL for the image using the filename, assuming that the image file is located at "static/img/"
    #     "image": url_for("static", filename= "img/" + user.img)}
    return user.__dict__

# APIs with JSON - sqlite3
@app.route("/departments")       # http://127.0.0.1:5000/departments
def get_all_departments():               
    departments = get_departments()

    # If you return a dict or list from a view, it will be converted to a JSON response.
    return [department.__dict__ for department in departments]


# HTTP Methods
def get_user():
    return UserProfile("Potter", "Gryffindor", "potter.jpeg")


# Sessions
# session object allows you to store information specific to a user from one request to the next. 
# This is implemented on top of cookies for you and signs the cookies cryptographically. 
# What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.

# When a user starts a session with a Flask application, a session ID (or session key) is created and stored in a cookie on the client's browser. 
# This session ID is used to identify the user's session on the server side. 
# The actual session data, including any parameters or values that the user has set, is "stored on the server".
# When the user sends subsequent requests to the Flask application, the server uses the session ID in the cookie to retrieve the corresponding session data from its storage. 
# This allows Flask to keep track of the user's session even as they navigate between different pages or make multiple requests.
# By default, Flask uses a secure and tamper-proof way to store the session ID in the cookie, using the session object's secret_key attribute. 
# This helps to prevent attacks such as session hijacking or session fixation. 


# Web applications use different HTTP methods when accessing URLs. 
# Option 1: You can use the methods argument of the route() decorator to handle different HTTP methods.
# By default, a route only answers to GET requests. 
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # session['username'] = "anonymous"
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    else:                               # http://127.0.0.1:5000/signin
        return '''<form method="POST" action="/signin">
    <input type="text" name=username>
    <input type="submit" value=Login>
    </form>'''    

# Option 2: You can also separate views for different HTTP Methods into different functions:
@app.get('/login')                      # http://127.0.0.1:5000/login
def login_get():
    return '''<form method="POST">
    <input type="text" name=username>
    <input type="submit" value=Login>
    </form>'''

@app.post('/login')
def login_post():
    return "do_the_login"


# Rendering Templates
# Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. 
# Because of that Flask configures the Jinja2 template engine for you automatically.
# Templates can be used to generate any type of text file. 
# For web applications, you’ll primarily be generating HTML pages, but you can also generate markdown, plain text for emails, any anything else.

@app.route('/hi/')                  # http://127.0.0.1:5000/hi
@app.route('/hi/<name>')            # http://127.0.0.1:5000/hi/Potter
def hello(name = None):
    return render_template('welcome.html', name = name)   # templates/welcome.html






# tell Flask to behave as though it’s handling a request even while we use a Python shell:
with app.test_request_context():
    print( url_for('index') )
    print( url_for('static', filename='hello.js') )             # /static/hello.js
    print( url_for('signin') )                                  # /signin
    print( url_for('show_post', postID=1) )                    # /post/1
    print( url_for('show_user_profile', username='John Doe') )  # /user/John%20Doe

class UserProfile:

    def __init__(self, username, house, img):
        self.username = username
        self.house = house
        self.img = img