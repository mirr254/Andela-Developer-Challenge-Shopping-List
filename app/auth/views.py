from app.user import User
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm


@auth.route("/register", methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add a user to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=form.password.data)
        

        # add new user to list        
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template if error occured
    return render_template('auth/register.html', form=form, title='Register')

@auth.route("/login", methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        pass       

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route("/logout")
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))