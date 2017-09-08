import unittest
from app.shoppinglist_ops import ShoppinglistManager

#a class to contain test cases for the shopping list
class ShoppingListTest( unittest.TestCase ):
    
    def setUp(self):
        self.shoppingList = ShoppinglistManager() 

    #method to test value types in addItem
    def test_deleteList_method_returns_error_for_nonInt(self):
        self.assertRaises(ValueError, self.shoppingList.deleteList,"one")

    #method to check if quantity arg is not a number
    def test_get_shopping_listObject_for_nonInt(self):
        self.assertRaises( ValueError, self.shoppingList.get_shopping_listObject, "rice")

    #method to check if price arg is not a number
    def test_addToDic_if_key_anInt(self):
        self.assertRaises( ValueError, self.shoppingList.addToDic, 4, "hundred")
