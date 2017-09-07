class UserManager(object):

    users = {}

    def login(self, email, password):     
        if email in self.users.keys():
            import pdb; pdb.set_trace()
            for usrs in self.users.values():
                if usrs.password == password:
                    return True
             

    def register(self,key, value):
        #check if dic is empty
        if not self.users:
            self.users[key] = value
        else:
            self.users.update(key=value)