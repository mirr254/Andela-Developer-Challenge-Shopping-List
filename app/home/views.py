from flask import render_template, redirect, url_for, flash
from app.auth.views import logged_in_user
from app.shoppingcart import ShoppingCart
from app.auth.views import logged_in_user
from .shoppinglist_form import ShoppingList

from . import home

shopping_lists = {}

#method to remove item from the cart
def removeItem(self, item_name):

    if isinstance( item_name, str):
        pass
    else:
        raise ValueError

#a method to calculate total cost
def calculatePrice(self, price, quantity):        
    total_amount = price * quantity
    return total_amount

############# routes or endpoints ################################

@home.route('/')
def homepage():
    
   # Render the homepage template on the / route

    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
def dashboard():

    #check if user is logged in
    if logged_in_user == None:
        flash("You must be logged in to access this page")
        return redirect( url_for('auth.login'))
    
    form = ShoppingList()
    if form.validate_on_submit():
        #insert to list
        item_id = len( shopping_lists ) + 1
        shopping_list = ShoppingCart(logged_in_user, form.item_name.data, form.price.data, 
                                        form.quantity.data, item_id)
        pass

        #
    
    #Render the dashboard template on the /dashboard route    
    return render_template('home/dashboard.html',form=form, title="Dashboard")