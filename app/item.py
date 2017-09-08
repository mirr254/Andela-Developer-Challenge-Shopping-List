from app.common_functions import get_random_id

class Item(object):
    def __init__(self, name, list_id):
        
        self.name = name
        self.id = get_random_id()
        self.list_id = list_id

    def update(self, name):
        
        if name is None or len(name) < 1:
            return "Item must have a name"

        if not isinstance(name, str):
            return "Item name must be a string"

        self.name = name 