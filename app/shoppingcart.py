from app.item import Item
from app.common_functions import get_random_id

class ShoppingCart(object): 
    
    def __init__(self,title,owner_email):

        self.title = title
        self.items = []
        self.owner_email = owner_email
        self.id = get_random_id()

    def add_item(self, item_name):
        
        if item_name is None or len(item_name) < 1:
            return "Item must have a name"

        if not isinstance(item_name, str):
            return "Item name must be a string"

        for item in self.items:
            if item.name == item_name:
                return item_name + ' already Exist'

        new_item = Item(item_name)
        self.items.append(new_item)

        return new_item.id

   

    def update(self, new_title):
        
        if new_title is None or len(new_title) < 1:
            return "Please add a title to shopping list"

        if not isinstance(new_title, str):
            return "List title must be a string"

        self.title = new_title

    def remove_item(self, item_id):
        
        if not isinstance(item_id, int):
            return "Item id must be an Integer"

        count = 0
        for item in self.items:
            if str(item.id) == str(item_id):
                self.items.pop(count)
                del item
                return True
            count += 1

        return "Item does not exist"

    def list_items(self):
        
        item_names = []
        for item in self.items:
            item_names.append(item.name)

        return item_names