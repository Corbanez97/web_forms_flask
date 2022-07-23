'''
To build a web form, you will create a subclass of the FlaskForm 
    base class, which you import from the flask_wtf package. 
        You also need to specify the fields you use in your form, 
            which you will import from the wtforms package.

You import the following fields from the WTForms library:

StringField: A text input.
TextAreaField: A text area field.
IntegerField: A field for integers.
BooleanField: A checkbox field.
RadioField: A field for displaying a list of radio buttons for the user to choose from.

In the line from wtforms.validators import InputRequired, Length, 
    you import validators to use on the fields to make sure the user 
        submits valid data. InputRequired is a validator you’ll use to ensure 
            the input is provided, and Length is for validating the length 
                of a string to ensure it has a minimum number of characters, 
                    or that it doesn’t exceed a certain length.
'''
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired, Length

