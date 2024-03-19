class User:
    def __init__(self, id, password):
        self.id=id
        self.password=password
        
    def setId(self, id):
        self.id=id
        
    def getId(self):
        return self.id
    
    def setPassword(self, password):
        self.password=password
        
    def getPassword(self):
        return self.password
    
    def printUser(self):
        print(f'ID: {self.id}, PW: {self.password}')