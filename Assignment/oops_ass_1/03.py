class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
    
    def get_area(self):
        print(f"Areae is: {self.__length*self.__breadth}")

r1 = Rectangle(20,30)
# r1.get_area()