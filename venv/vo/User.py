class User:
    def __init__(self, id=None, password=None):
        self.id=id
        self.password=password
    
    def getId(self):
        return self.id
    
    def getPassword(self):
        return self.password