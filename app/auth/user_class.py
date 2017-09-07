#this script handles the operations to be performed on user accounts
#for example adding user or deleting user

class User(object):

    def __init_(self):
        pass

    def __init_(self, email, first_name, last_name, password):

        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def login(self, email, password):
        if len(password) < 1:
            print("Password cannot be blank")
        if isinstance(email, str):
            if 
            

    def addToDic(self,key, value):
        if key not in self.users.keys():
            self.users.setdefault(key, []) #if shopping list is empty set slist[key]=default
        self.users[key].append(value)
        return self.users
