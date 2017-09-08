class UserManager(object):

    users = {}

    def login(self, email, password):
        types = int, float
        if isinstance(email, types):
            raise ValueError   
        if email in self.users.keys():            
            for usrs in self.users.values():
                if usrs.password == password:
                    return True
             

    def register(self,key, value):
        if not key:
            return("Key cannot be blank")
        if not value:
            return("Value cannot be blank")
        #check if dic is empty
        if not self.users:
            self.users[key] = value
        else:
            self.users.update(key=value)