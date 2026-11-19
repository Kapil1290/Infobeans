from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Meouw")

class Dog(Animal):
    def sound(self):
        print("Barking")
    
class Cow(Animal):
    def sound(self):
        print("Mahhhhhhhhhh")

c = Cat().sound()
c = Cow().sound()

