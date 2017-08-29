#use flask-WTF form
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, BooleanField, PasswordField, SubmitField, StringField
from wtforms import validators, ValidationError


#a class for signup or registration
class UserRegistrationForm(FlaskForm):

    fname = StringField("First Name", [validators.InputRequired()])
    lname = StringField("Last Name", [validators.InputRequired()])
    email = StringField('Email Address', [validators.InputRequired(), 
                       validators.Email("Please provide a valid email")])
    password = PasswordField("password", [validators.InputRequired()])
    password_confirm = PasswordField("Confirm password", [validators.InputRequired()])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])
    submit = SubmitField("Signup")

#Admin registration will inherit from the UserRegistrationForm since admin is also a user but with 
#rights
class AdminRegistration( UserRegistrationForm ):

    #user level 1 is admin and 2 is normal user
    level = IntegerField('User Level', [validators.NumberRange(min=0, max=10)]) 

#Sign in class inherit from UserRegistration and use only required fields
class SignIn(UserRegistrationForm):