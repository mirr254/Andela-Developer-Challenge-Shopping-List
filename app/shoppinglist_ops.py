from flask import session
class ShoppinglistManager(object):

   
    all_shopping_list = []

    def __init__(self):
        pass       


    #method to remove item from the cart
    def removeItem(self,item_name):

        if isinstance( item_name, str):
            pass
        else:
            raise ValueError

    def addToDic(self,key, value):
        shopping_lists= {}
        shopping_lists.setdefault(key, [])
        shopping_lists[key].append(value)
        self.all_shopping_list.append(shopping_lists)
        return self.all_shopping_list

    def get_shopping_list(self,list_id):
        if isinstance(list_id, int):
            for all_list in self.all_shopping_list:
                print(all_list)
                if list_id in all_list[session["email"]].id:
                    #value exists update
                    return all_list[session["email"]]