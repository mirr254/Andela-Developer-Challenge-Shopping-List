#use flask-WTF form
from flask_wtf import Form
from wtforms import TextField, IntegerField, BooleanField, PasswordField, SubmitField

from wtforms import validators, ValidationError

#Sign in class

class SignIn( Form ):
    #email field
    email = TextField("Email", [validators.Required("Enter Email to sign in"), 
        validators.Email("Please enter a valid Email Address")])

    #password field
    password = PasswordField("Password", [validators.Required("Password to login")])

    #remember me
    rem_me = BooleanField("remember_me", default=False)

    #submit action 
    submit = SubmitField("Sign in")