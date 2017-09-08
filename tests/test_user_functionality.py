#This class is used to build test cases for user functionalities like addUser and deleteUser 
import unittest
from app.auth.user_ops import UserManager
from app.models import addUser

class UserFunctionalityTests( unittest.TestCase):

    #initialize the User class
    def setUp(self):
        self.user = UserManager()

    #assert that email in login is not int
    def test_login_email_for_int(self):
        self.assertRaises( ValueError, self.user.login, 123, "ertgf")

    def test_login_email_for_int_if_pass_is_allInt(self):
        self.assertRaises( ValueError,self.user.login, 123, 1234)

    def test_login_email_for_int_if_passwrd_is_mixed(self):
        self.assertRaises( ValueError, self.user.login, 123, "1234ertgf")

