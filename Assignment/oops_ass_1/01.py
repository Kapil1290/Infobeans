
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def display_detail(self):
        return self.__name, self.__age


p1 = Person("Kapil", 21)
p2 = Person("Sitaram", 22)
name, age = p1.display_detail()
# print(f"Object 1\nName: {name}\nAge: {age}\n")

name, age = p2.display_detail()
# print(f"Object 2\nName: {name}\nAge: {age}")
