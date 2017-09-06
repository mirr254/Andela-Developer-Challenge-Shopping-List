class Item(object):
    def __init__(self, name):
        """
            Attributes:
                name (str): Name of the item
                id (str): A unique identifier for each item.
            Methods:
                update
            Args:
                name (str): A unique name for each item.
            """
        self.name = name
        self.id = global_functions.get_random_id()

    def update(self, name):
        """This function changes the name of an item
                Args:
                    name (str): new name of the item.
                Returns:
                    error message if name is not valid
            """
        if name is None or len(name) < 1:
            return "Item must have a name"

        if not isinstance(name, str):
            return "Item name must be a string"

        self.name = name