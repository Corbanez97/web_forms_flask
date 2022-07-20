'''
We first import the Flask object from the flask package.
We then use it to create your Flask application instance, giving it the name app. 
The, we pass the special variable __name__, which holds the name of the current Python module. 
This name tells the instance where it is located; 
Tis is needed because Flask sets up some paths behind the scenes.
'''
##Intro Section
from markupsafe import escape
import datetime
from flask import Flask, render_template #render_template to... render... a template... ☜(ﾟヮﾟ☜)
from flask import request, url_for, flash, redirect
'''
*The global request object to access incoming request data 
    that will be submitted via the HTML form you built in the last step.
*The url_for() function to generate URLs.
*The flash() function to flash a message when a request 
    is processed (to inform the user that everything went well, 
        or to inform them of an issue if the submitted data is not valid).
*The redirect() function to redirect the client to a different location.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

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

@app.route('/about_app/')
def about_app():
    '''
    This function is decorated with the @app.route() decorator that 
    transforms it into a view function that handles requests 
    for the http://127.0.0.1:5000/about_app endpoint.
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

##Template Section
@app.route('/index/')
def index():
    '''
    This function is running a render_template function which open templates from
    a template folder located inside the flask_app directory
    '''
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/date/')
def show_datetime():
    '''
    On the html we added an H3 heading with the 
    special {{ ... }} delimiter to print the value 
    of the dt_now variable.
    '''
    dt_now = datetime.datetime.now()
    return render_template('date.html', dt_now = dt_now)

@app.route('/comments/')
def comments():
    comments = ['This is being printed recursively', 'Line by line', 'Using jinja2', 'Looping capabilities']
    footnote = ['This is being', 'Joined by', 'A Jinja filter']
    return render_template('comments.html', comments = comments, footnote = footnote)

##Forms section

messages = [    
            {'title': 'Message One', 'body': 'This is a dictionary'},
            {'title': 'Message Two', 'body': 'This is another entry on the same dictionary'}
            ]

@app.route('/message/')
def message():
    return render_template("message.html", messages = messages)

@app.route('/create/', methods = ('GET', 'POST')) #This adds a POST method. Therefore, this page is capable of submiting data
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        if not title:
            flash('Title is required!')
        elif not body:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'body': body})
            return redirect(url_for('message'))
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug = True)