class ShoppingList(object): 

    cart = {} # A dictionary to hold item_name:price as key:value 
    balance = 0
    budget_amount = 0 #one wouldn't want to shop for more than is available

    def __init__(self, budget_amount):
        self.budget_amount = budget_amount        

    #a method to add items to the cart dictionary
    def addItem(self, item_name, price, quantity):
        #declare arguement types and check they are use correctly
        number_types = ( int, float, complex)

        if isinstance(price, number_types) and isinstance(quantity, number_types) and isinstance(item_name, str):
            self.cart[item_name] = price

            total_cost = self.calculatePrice(price, quantity)

            self.balance = self.budget_amount - total_cost
        else:
            raise ValueError
    
    #method to remove item from the cart
    def removeItem(self, item_name):

        if isinstance( item_name, str):
            pass
        else:
            raise ValueError

    #a method to calculate total cost
    def calculatePrice(self, price, quantity):
        
        total_amount = price * quantity
        #check total doesnt exceed balance we have
        if total_amount > self.balance:
            print("That amount is more than what we have")
            return 0

        return total_amount