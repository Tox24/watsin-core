import uuid

class Item():
    """ Superclass for the different types of Item """
    
    def __init__(self):
        self.id = str(uuid.uuid8())
    
class FoodItem(Item):
    """ Class for the Items which are food 
        Args: "name"
    """
    def __init__(self, name):
        self.name = name
    