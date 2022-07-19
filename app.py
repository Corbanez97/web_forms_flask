'''
We first import the Flask object from the flask package.
We then use it to create your Flask application instance, giving it the name app. 
The, we pass the special variable __name__, which holds the name of the current Python module. 
This name tells the instance where it is located; 
Tis is needed because Flask sets up some paths behind the scenes.
'''
from markupsafe import escape
import datetime
from flask import Flask, render_template #render_template to... render... a template... ☜(ﾟヮﾟ☜)

app = Flask(__name__)

@app.route('/')
def hello():
    '''
    Once you create the app instance, you can use it to handle incoming 
    web requests and send responses to the user. @app.route is a decorator that 
    turns a regular Python function into a Flask view function, 
    which converts the function’s return value into an HTTP response to be displayed by an HTTP client, 
    such as a web browser. 
    You pass the value '/' to @app.route() to signify that 
    this function will respond to web requests for the URL /, which is the main URL.
    The hello() view function returns the string '<h1>Hello, World!</h1>' as an HTTP response.
    '''
    return '<h1>Hello, World!<h1>'

@app.route('/about/')
def about():
    '''
    This function is decorated with the @app.route() decorator that 
    transforms it into a view function that handles requests 
    for the http://127.0.0.1:5000/about endpoint.
    '''

    return '<h2>This is a flask web application.<h2>'

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    '''
    This is a dynamic route that adds two numbers together and displays the result.
    '''
    return f'<h1>{n1 + n2}<h1>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    '''
    To display user data safely, use the escape() function that 
    comes with the markupsafe package, which was installed along with Flask.
    '''
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/index/')
def index():
    '''
    This function is running a render_template function which open templates from
    a template folder located inside the flask_app directory
    '''
    return render_template('index.html')

@app.route('/index/date/')
def show_datetime():
    return render_template('date.html', dt_now = datetime.datetime.now())

if __name__ == '__main__':
    app.run(debug = True)