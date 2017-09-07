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
            self.shopping_lists.setdefault(key, []) #if shopping list is empty set slist[key]=default
        self.shopping_lists[key].append(value)
        
        #self.all_shopping_list.append(self.shopping_lists)
        return self.shopping_lists

    def get_shopping_listObject(self,list_id):
       
        if isinstance(list_id, int):
            for all_list in self.shopping_lists:                
                if list_id in all_list[session["email"]].id:
                    #value exists for update
                    print(all_list)
                    return all_list[session["email"]]

    def deleteList(self, list_id):
        if isinstance(list_id, int):
            list_to_delete = self.get_shopping_listObject(list_id)
            print(list_to_delete)
            return True

            