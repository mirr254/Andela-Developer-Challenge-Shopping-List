#use flask-WTF form
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, BooleanField, PasswordField, SubmitField

from wtforms import validators, ValidationError

#Sign in class

class SignIn(FlaskForm):
    #username and password for login
    email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter a valid Email.")])
    password = PasswordField("Password")
