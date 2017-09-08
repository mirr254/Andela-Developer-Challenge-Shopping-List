from flask import session

class ItemManager(object):

    items = {}

    def update(self, name):
        
        if name is None or len(name) < 1:
            return "Item must have a name"

        if not isinstance(name, str):
            return "Item name must be a string"

        self.name = name

    
    def addToDic(self,key, value):
        if isinstance(key, str):
            self.items.setdefault(key, []).append(value)
            return self.items
        else:
            raise ValueError
        

    def get_item_listObject(self,item_id):       
        if isinstance(item_id, int):
            for all_list in self.items[session["email"]]:              
                if item_id == all_list.id:
                    #value exists for update                    
                    return all_list
        else:
            raise ValueError