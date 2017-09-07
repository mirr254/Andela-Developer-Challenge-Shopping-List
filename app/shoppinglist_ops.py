from flask import session
class ShoppinglistManager(object):

   
    #all_shopping_list = []
    shopping_lists= {}

    def __init__(self):
        pass       


    #method to remove item from the cart
    def removeItem(self,item_name):

        if isinstance( item_name, str):
            pass
        else:
            raise ValueError

    def addToDic(self,key, value):
        if key not in self.shopping_lists.keys():
            self.shopping_lists.setdefault(key, [])
        self.shopping_lists[key].append(value)
        print(self.shopping_lists)
        #self.all_shopping_list.append(self.shopping_lists)
        return self.shopping_lists

    def get_shopping_list(self,list_id):
        print(self.shopping_lists)
        if isinstance(list_id, int):
            # for all_list in self.all_shopping_list:                
            #     if list_id in all_list[session["email"]].id:
            #         #value exists update
            #         return all_list[session["email"]]
            pass