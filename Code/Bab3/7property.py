class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius harus positif")
        self._radius = value
    
    @property
    def area(self):
        return 3.14 * self.radius ** 2
    
c = Circle(5)
print(c.radius) # Output: 5
print(c.area)   # Output: 78.5

c.radius = 10
print(c.radius) # Output: 10
print(c.area)   # Output: 314.0

#c.radius = -5   # Akan menimbulkan ValueError karena radius harus positif
