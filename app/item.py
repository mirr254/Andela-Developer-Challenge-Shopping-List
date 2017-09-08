from app.common_functions import get_random_id

class Item(object):
    def __init__(self, item_name, list_id):
        
        self.item_name = item_name
        self.id = get_random_id()
        self.list_id = list_id
 