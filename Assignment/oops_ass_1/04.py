class Circle2:
    def __init__(self, radius):
        self.__radius = radius
    
    def get_circum(self):
        print(f"Circumstance: {3.14*self.__radius}")

c1 = Circle2(23)
# c1.get_circum()