class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Cat(Animal):
    def __init__(self, name, legs, color):
        super().__init__(name, legs)
        self.color = color

    def meow(self):
        print(f"{self.name} is meowing.")

class Dog(Animal):
    def __init__(self, name, legs, breed):
        super().__init__(name, legs)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")
