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
from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)
app.config["DEBUG"] = True

# Modern web applications use meaningful URLs to help users. 
# Use the route() decorator to bind a function to a URL.
@app.route("/")
def index():
    return "hello, there!"  # The default content type is HTML

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


@app.route("/userprofile")       # http://127.0.0.1:5000/userprofile
def me_api():               
    user = get_user()
    return {
        "username": user.username,
        "house": user.house,
        # Generate the URL for the image using the filename, assuming that the image file is located at "static/img/"
        "image": url_for("static", filename= "img/" + user.img),
    }

def get_user():
    return UserProfile("Potter", "Gryffindor", "potter.jpeg")

# Web applications use different HTTP methods when accessing URLs. 
# Option 1: You can use the methods argument of the route() decorator to handle different HTTP methods.
# By default, a route only answers to GET requests. 
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return "do_the_signin()"
    else:
        return "show_the_signin_form()"     # http://127.0.0.1:5000/signin

# Option 2: You can also separate views for different HTTP Methods into different functions:
@app.get('/login')                  # http://127.0.0.1:5000/login
def login_get():
    return "show_the_login_form"

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