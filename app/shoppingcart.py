class ShoppingCart(object): 
    
    def __init__(self,owner_email, item_name, price, quantity, item_id):
        self.owner_email = owner_email
        self.item_name = item_name
        self.price = price
        self.quantity = quantity      
        self.item_id = item_id