#this script handles the operations to be performed on user accounts
#for example adding user or deleting user
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

system_users = {}

class User(object): 
    
    def __init__(self, fname, email, password):

        self.f_name = fname               
        self.email = email
        self.password = password

    #a function to delete user depending given id
    def deleteUser(self, userID):
        #make sure user id is a number
        if isinstance( userID, int):
            #check if user exists then delete            
            pass
        else:
            raise ValueError

#add user
def addUser(fname, email, password):

    if not password:
        return "password cannot be blank"

    if isinstance(fname, str) and isinstance(email, str):
        new_usr = User(fname, email, password)
        system_users[email] = new_usr
    else:
        raise ValueError

    
