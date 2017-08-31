#this script handles the operations to be performed on user accounts
#for example adding user or deleting user
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


system_users = {}

shoppingCart = {}

class User(object): 
    
    def __init__(self, fname, email, password):
        
        self.f_name = fname               
        self.email = email #since it will be unique, it will be used as id
        self.password = password

    #a function to delete user depending given id
    def deleteUser(self, email):
        #make sure user id is a number
        if isinstance( email, str):
            #check if user exists then delete            
            if email in system_users.keys():
                system_users.pop(email) #maintains mutability

        else:
            raise ValueError

################################## end of user class #####################################

class ShoppingList(object):

    def __init__():
        pass



#add user
def addUser(fname, email, password):

    if password == "":
        raise ValueError

    if isinstance(fname, str) and isinstance(email, str):
        new_usr = User(fname, email, password)
        system_users[email] = new_usr
    else:
        raise ValueError


"""
check if user exists

key = email

"""
def checkKeyValuePairExistence(dic, key, value):
    try:
        return dic[key] == value
    except KeyError:
        return False
