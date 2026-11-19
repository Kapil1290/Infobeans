from abc import ABC, abstractmethod

# Partial Abstract 
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
        super(Dog, self).__init__(color)
    
    def show_color(self):
        print(super().get_color())

d1 = Dog("red", "labra")
d1.show_color()


# Fully Abstraction
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @property
    @abstractmethod
    def type_of_vehicle(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car is starting....")
    def stop(self):
        print("Car stopped...")
    type_of_vehicle = "cng"
class Truck(Vehicle):
    def start(self):
        print("Truck is starting....")
    def stop(self):
        print("Truck stopped...")
    type_of_vehicle = "Diesal"

truck = Truck()
truck.start()
truck.stop()
print(truck.type_of_vehicle)




    