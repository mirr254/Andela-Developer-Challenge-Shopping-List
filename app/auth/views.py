from app.user import User
from flask import flash, redirect, render_template, url_for, session
from . import auth
from .forms import LoginForm, RegistrationForm

users = {}


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
        session['email'] = user.email
        session['logged_in'] = True
        return redirect( url_for('home.dashboard'))

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
        if form.email.data in users.keys(): #email is correct
            user_account = users[ form.email.data ]

            #check if password exists
            if user_account.password == form.password.data:
                # user sessions to keep track of logged in user   
                session['email'] = user_account.email
                session['logged_in'] = True
                return redirect( url_for('home.dashboard'))
            
            flash("Sorry, password or email incorrect")
            #redirect to the login page
            return redirect(url_for('auth.login'))

        flash("Sorry, password or email incorrect")
        #redirect to the login page
        return redirect(url_for('auth.login'))

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route("/logout")
def logout():
    """
    Handle requests to the /logout route
    Log a user out through the logout link
    """
    session["logged_in"] = None
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))