class UserManager(object):

    users = {}

    def login(self, email, password):        
        if email in self.users.keys() and self.users[email].password:
            return True  

    def register(self,key, value):
        if key not in self.users.keys():
            self.users.setdefault(key, []) #if shopping list is empty set slist[key]=default
        self.users[key].append(value)