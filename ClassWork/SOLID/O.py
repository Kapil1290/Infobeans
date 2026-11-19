from abc import ABC, abstractmethod

# Open/Close Modification

class Laptop(ABC):
    @abstractmethod
    def cpu(self):
        pass

    @abstractmethod
    def trackpad(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

class Asus(Laptop):
    def cpu(self):
        print("CPU-Nvidia")

    def trackpad(self):
        print("yes")
    
    def keyboard(self):
        print("yes")

        