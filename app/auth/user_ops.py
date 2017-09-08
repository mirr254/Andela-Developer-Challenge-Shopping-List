class UserManager(object):

    users = {}

    def login(self, email, password):
        types = int, float
        if isinstance(email, types):
            raise ValueError   
        if email in self.users.keys():                     
            for usrs_obj_list in self.users[email]:
                if usrs_obj_list.password == password:
                    return True
            
             

    def register(self,key, value):
        if not key:
            return("Key cannot be blank")
        if not value:
            return("Value cannot be blank")
        #check if dic is empty
        if key not in self.users.keys():
            self.users.setdefault(key, []).append(value)            
            return True
        else:
            return False
    