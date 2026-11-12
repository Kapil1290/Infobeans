
class Traffic:
    def __init__(self, color, duration):
        self.__color = color
        self.__duration = duration
    
    def change_color(self, color):
        self.__color = color
    
    def check_color(self):
        print(f"Current light is: {self.__color}")

t1 = Traffic("Red", "30 Sec")
t1.change_color("Green")
# t1.check_color()




