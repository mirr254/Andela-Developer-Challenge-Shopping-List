#this script handles the operations to be performed on user accounts
#for example adding user or deleting user
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


class User(object):

    def __init__(self,userID, fname,lname, email, password):
            self.user_id = userID
            self.f_name = fname
            self.l_name = lname        
            self.email = email
            self.password = password    
            

    
    def __repr__(self):
        return '<User %r>' % self.email
            

    #a function to delete user depending given id
    def deleteUser(self, userID):
        #make sure user id is a number
        if isinstance( userID, int):
            #check if user exists then delete            
            pass
        else:
            raise ValueError
