#This class is used to build test cases for user functionalities like addUser and deleteUser 
import unittest
from app.user import User

class UserFunctionalityTests( unittest.TestCase):

    #initialize the User class
    def setUp(self):
        self.user = User()

    #check whether the method to delete user only accepts int type id
    def test_if_deleteUser_accepts_intID(self):
        self.assertRaises( ValueError, self.user.deleteUser, "two")

    #test addUser pass is not empty
    def

