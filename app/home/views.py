from flask import render_template, redirect, url_for, flash, session, request
from app.shoppingcart import ShoppingCart
from app.item import Item
from .shoppinglist_form import ShoppingList
from app.shoppinglist_ops import ShoppinglistManager
from app.item_ops import ItemManager
from .list_item_form import itemForm

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
    if not session["logged_in"] == False:
        flash("You must be logged in to access this page")
        return redirect( url_for('auth.login'))
    
    form = ShoppingList()
    if form.validate_on_submit():
        #create a new shopping list
        shopping_cart = ShoppingCart( form.title.data, session['email'])
        
        new_shopping_cart = ShoppinglistManager().addToDic(session["email"], shopping_cart)
        flash("List saved okay")
        return render_template('home/dashboard.html', title="Dashboard", new_shopping_cart=new_shopping_cart)

    #Render the new lis template on the /dashboard route    
    return render_template('home/newlist.html',form=form, title="Add new")

@home.route('/update/shopping-list/<_ids>', methods=['POST', 'GET'])
def update_shoppinglist(_ids):

    #check if user is logged in
    if not session["logged_in"] == False:
        flash("You must be logged in to access this page")
        return redirect( url_for('auth.login'))

    # get selected shoppinglist
    ids = int(_ids)
    shoppinglist = ShoppinglistManager().get_shopping_listObject(ids)    
    form_object = shoppinglist
    
    form = ShoppingList(obj=form_object)
    if form.validate_on_submit():
        form.populate_obj(form_object)
        return redirect(url_for('home.dashboard'))

    return render_template('home/newlist.html',form=form, title="Update")


@home.route('/delete/shopping-list/<_ids>', methods=['POST', 'GET'])
def delete_shoppinglist(_ids):

    #check if user is logged in
    if not session["logged_in"] = False:
        flash("You must be logged in to access this page")
        return redirect( url_for('auth.login'))

    # get selected shoppinglist
    ids = int(_ids)
    is_deleted = ShoppinglistManager().deleteList(ids)
    if is_deleted == True:
        flash("Item deleted successfully")
        return redirect(url_for('home.dashboard'))

    # return render_template('home/newlist.html',form=form, title="Update")



@home.route('/dashboard')
def dashboard():
    #check if user is logged in
    if not session["logged_in"] == False:
        flash("You must be logged in to access this page")
        return redirect( url_for('auth.login'))

    new_shopping_cart = ShoppinglistManager.shopping_lists
    return render_template("home/dashboard.html", title="Dashboard", new_shopping_cart=new_shopping_cart )

# @home.route('/shoppinglist/<list_id>/add-item', methods=['POST', 'GET'])
# def new_item(list_id):

#     list_id_int = int(list_id)

#     form = itemForm()
#     if form.validate_on_submit():
#         item = Item(name=form.data.name, list_id_int)
#         new_item = ItemManager().addToDic(list_id_int, item)
#         flash("Item saved")

    
#     #Render the newitem template on the /dashboard route    
#     return render_template('home/newitem.html',form=form, title="Add new")