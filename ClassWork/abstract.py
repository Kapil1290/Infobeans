from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, color):
        self.__color = color

    @abstractmethod
    def show_color(self):
        pass
    
    def get_color(self):
        return self.__color

class Dog(Animal):
    def __init__(self, color, name):
        self.__name = name
        super(self,).__init__(color)
    
    def show_color(self):
        print(self.get_color())

d1 = Dog("red", "labra")
d1.show_color()
    