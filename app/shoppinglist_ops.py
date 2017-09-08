from flask import session
class ShoppinglistManager(object): 
   
    #all_shopping_list = []
    shopping_lists= {}

    def addToDic(self,key, value):
        if isinstance(key, str):
            self.shopping_lists.setdefault(key, []).append(value)
            return self.shopping_lists
        else:
            raise ValueError
        

    def get_shopping_listObject(self,list_id):       
        if isinstance(list_id, int):
            for all_list in self.shopping_lists[session["email"]]:              
                if list_id == all_list.id:
                    #value exists for update                    
                    return all_list
        else:
            raise ValueError

    def deleteList(self, list_id):
        
        if isinstance(list_id, int):            
            value_to_delete = self.get_shopping_listObject(list_id)           
            new_dic_after_delete = {key:val for key, val in self.shopping_lists.items() if val == value_to_delete }            
            self.shopping_lists = new_dic_after_delete                            
            return True
        else:
            raise ValueError

            