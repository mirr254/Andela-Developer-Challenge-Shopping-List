from flask import render_template, redirect, url_for, flash, session, request
from app.shoppingcart import ShoppingCart
from .shoppinglist_form import ShoppingList
from app.shoppinglist_ops import ShoppinglistManager

from . import home  


############# routes or endpoints ################################

@home.route('/')
def homepage():
    return redirect(url_for('auth.login'))
    
   # Render the homepage template on the / route


    return render_template('home/index.html', title="Welcome")


@home.route('/lists', methods=['POST', 'GET'])
def newShoppinglist():

    #check if user is logged in
    # if not session["logged_in"]:
    #     flash("You must be logged in to access this page")
    #     return redirect( url_for('auth.login'))
    
    form = ShoppingList()
    if form.validate_on_submit():
        #create a new shopping list
        shopping_cart = ShoppingCart( form.title.data, session['email'])
        
        new_shopping_cart = ShoppinglistManager().addToDic(session["email"], shopping_cart)
        #import pdb; pdb.set_trace()
        flash("List saved okay")
        return render_template('home/dashboard.html', title="Dashboard", new_shopping_cart=new_shopping_cart)

    #Render the dashboard template on the /dashboard route    
    return render_template('home/newlist.html',form=form, title="Add new")

@home.route('/update/shopping-list/<_ids>', methods=['POST', 'GET'])
def update_shoppinglist(_ids):  

    # get selected shoppinglist
    ids = int(_ids)
    shoppinglist = ShoppinglistManager().get_shopping_listObject(ids)
    import pdb; pdb.set_trace()   
    form_object = shoppinglist
    #import pdb; pdb.set_trace()
    
    form = ShoppingList(obj=form_object)
    if form.validate_on_submit():
        form.populate_obj(form_object)
        return redirect(url_for('home.dashboard'))

    return render_template('home/newlist.html',form=form, title="Update")


@home.route('/delete/shopping-list/<_ids>', methods=['POST', 'GET'])
def delete_shoppinglist(_ids):  

    # get selected shoppinglist
    ids = int(_ids)
    is_deleted = ShoppinglistManager().deleteList(ids)
    if is_deleted == True:
        flash("Item deleted successfully")
        return redirect(url_for('home.dashboard'))

    # return render_template('home/newlist.html',form=form, title="Update")



@home.route('/dashboard')
def dashboard():
    # if session["logged_in"] == True:        
    #     return render_template("home/dashboard.html" )
    #else:
    #flash("You must be logged in to access this page")
    #return redirect(url_for('auth.login') )
    new_shopping_cart = ShoppinglistManager.shopping_lists
    return render_template("home/dashboard.html", title="Dashboard", new_shopping_cart=new_shopping_cart )
