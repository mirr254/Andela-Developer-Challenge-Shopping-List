#this script handles the operations to be performed on user accounts
#for example adding user or deleting user

class User(object):

    #initialize the class
    def __init__(self):
        pass

    #a fucntion to add users
    def addUser(self,userID, fname,lname, img_url, email, password):
        self.user_id = userID
        self.f_name = fname
        self.l_name = lname
        self.img_url = img_url
        self.email = email
        self.password = password

    #a function to delete user depending given id
    def deleteUser(self, userID):
        #make sure user id is a number
        if isinstance( userID, int):
            #check if user exists then delete 
            
            pass
