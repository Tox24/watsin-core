from typing import List, Any
from Items import Item, FoodItem

class Inventory():
    """ Inventory class """
    
    def __init__(self, name: str, capacity: int, items: List[Item] = []):
        self.name: str = name
        self.capacity: int = capacity
        self.items: List[Item] = items
        
    def add_item(self, items: List[Item]):
        self.items = self.items + items
        
    def modify(self, **kwargs):
        for attr_name, new_value in kwargs.items:
            if hasattr(self, attr_name):
                setattr(self, attr_name, new_value)