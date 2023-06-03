class Person(): 
    def __init__(self, name, salary):
        self.__name = name #variabel private
        self.__salary = salary #variabel private


oPerson1 = Person('Joe Schmoe', 90000) 
oPerson2 = Person('Jane Smith', 99000)

#akses nilai variabel salary secara langsung
print(oPerson1.salary) 
