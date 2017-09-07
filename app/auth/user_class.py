#this script handles the operations to be performed on user accounts
#for example adding user or deleting user
class Userr(object):

    def __init__(self, username, email, f_name, l_name, password):
        self.username = username
        self.email = email
        self.f_name = f_name
        self.l_name = l_name
        self.password = password