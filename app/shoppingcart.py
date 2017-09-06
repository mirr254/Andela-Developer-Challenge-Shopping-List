class ShoppingCart(object): 
    
    def __init__(self,title):
         """
            Attributes:
                title (str): A unique caption for each shopping list.
                items(list): A list to hold items in this shopping list
                id (int): a unique identifier for each shoppinglist
            Methods:
                add_item
                update
                remove_item
                list_items
            Args:
                title (str): A unique caption for each shopping list.
            """

        self.title = title
        self.items = []
        self.id = global_functions.get_random_id()

    def add_item(self, item_name):
        """ Creates a new Item object and appends it to list of items in this shoppinglist
            Args:
                item_name: The name of the new item to be created
            Returns:
                id of the new Item if it has been created successfully, otherwise returns the
                error message generated
        """
        if item_name is None or len(item_name) < 1:
            return "Item must have a name"

        if not isinstance(item_name, str):
            return "Item name must be a string"

        for item in self.items:
            if item.name == item_name:
                return 'Item ' + item_name + ' already added'

        new_item = Item(item_name)
        self.items.append(new_item)

        return new_item.id

    def update(self, new_title):
        """ Changes the title of a shoppinglist
            Args:
                new_title: The new caption of this shoppinglist
            Returns:
                None if title has been changed, otherwise returns the
                error message generated
        """
        if new_title is None or len(new_title) < 1:
            return "Shopping list must have a title"

        if not isinstance(new_title, str):
            return "Shopping list title must be a string"

        self.title = new_title

    def remove_item(self, item_id):
        """ Deletes the selected item object from memory
            Args:
                item_id (str): The unique identifier(id) of the item to be deleted
            Returns:
                True if the item has been deleted successfully, otherwise return the error message
        """
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
        """
            Returns:
                list: a list of all the items in this shoppinglists
        """
        item_names = []
        for item in self.items:
            item_names.append(item.name)

        return item_names