class App():
    """App class for instanciate a new App instance"""
    
    def __init__(self, name = "test"):
        """The init function for App class.

        Args:
            name (str, optional): _description_. Defaults to "test".
        """
        self.inventory_name = name
    
    def compile(self):
        pass
    
    def toy_func(self):
        print('aaaaaaaaaaaaa' * 5)
    
app = App()