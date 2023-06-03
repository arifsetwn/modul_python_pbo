class Example():

    def __init__(self, startingValue):
        self._x = startingValue
    
    @property 
    def x(self): # this is the decorated getter method 
        return self._x
    
    @x.setter 
    def x(self, value): 
        self._x = value

oExample = Example(10) 
print(oExample.x) 
oExample.x = 20