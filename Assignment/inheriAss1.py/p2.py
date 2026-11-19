from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass

class Car(Vehicle):
    def start(self):
        print("button")
    def stop(self):
        print("car stopped")

class Bus(Vehicle):
    def start(self):
        print("ignition")
    def stop(self):
        print("bus stopped")

class Bike(Vehicle):
    def start(self):
        print("kick")
    def stop(self):
        print("bike stopped")

c = Car().start()
b = Bus().start()