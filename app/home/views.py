from flask import render_template
from .shoppinglist_form import ShoppingList

from . import home

@home.route('/')
def homepage():
    
   # Render the homepage template on the / route

    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
def dashboard():
    
    form = ShoppingList()
    if form.validate_on_submit():
        #insert to list
        pass

        #
    
    #Render the dashboard template on the /dashboard route    
    return render_template('home/dashboard.html',form=form, title="Dashboard")