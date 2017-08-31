#This class is used to build test cases for user functionalities like addUser and deleteUser 
import unittest
from app.user import User
from app.models import addUser

class UserFunctionalityTests( unittest.TestCase):

    #initialize the User class
    def setUp(self):
        self.user = User()
        self.add_user = addUser

    #check whether the method to delete user only accepts int type id
    def test_if_deleteUser_accepts_intID(self):
        self.assertRaises( ValueError, self.user.deleteUser, "two")

    #test addUser pass is not int
    def test_if_param1_is_string(self):
        self.assertRaises(ValueError, self.add_user, 2,"sam","kung")

    #test addUser pass is not int
    def test_if_param2_is_string(self):
        self.assertRaises(ValueError, self.add_user, "first", 2,"kung")

    #test addUser pass is not empty
    def test_if_param3_is_empty(self):
        self.assertRaises(ValueError, self.add_user, 2,"sam",[])

