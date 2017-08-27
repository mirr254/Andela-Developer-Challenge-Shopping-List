import unittest
from app.shoppingcart import ShoppingList

#a class to contain test cases for the shopping list
class ShoppingListTest( unittest.TestCase ):

    def setUp(self):
        budget_amount = 500
        self.shoppingList = ShoppingList(budget_amount)

    #method to test value types in addItem
    def test_addItem_method_returns_error_for_nonInt(self):
        self.assertRaises(ValueError, self.shoppingList.addItem, 1, "one", "thirty")

    #method to check if quantity arg is not a number
    def test_addItem_method_returns_error_for_quantityArg_string(self):
        self.assertRaises( ValueError, self.shoppingList.addItem, "rice", "four", 400)

    #method to check if price arg is not a number
    def test_addItem_method_returns_error_for_priceArg_string(self):
        self.assertRaises( ValueError, self.shoppingList.addItem, "Water", 4, "hundred")
    

    #tests for remove item
    #check if arg is a string
    def test_removeItem_method_returns_error_for_numbers(self):
        self.assertRaises( ValueError, self.shoppingList.removeItem, 2)


    #check if calculatePrice raises an error if total cost exceeds budget cost
    def test_calculatePrice_returns_err_for_exceedingBudget(self):
        result = self.shoppingList.calculatePrice( 2, 150)
        self.assertGreaterEqual(self.shoppingList.balance, result)
