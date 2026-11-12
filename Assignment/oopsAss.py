class Employee:
    def setter_details(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary
    
    def display(self):
        return self.__dict__

emp1 = Employee()
emp1.setter_details("Kapil",1,12000)
emp2 = Employee()
emp2.setter_details("Sitaram",2,23000)
# print(emp2.display())



class Book:
    def setter_details(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def display_detail(self):
        return self.__dict__
b1 = Book()
b1.setter_details("The last lesson", "Arvind Jaiswal", 450)
# print(b1.display_detail())


class BankAccount:
    def set_detail(self, account_name, holder_name, balance):
        self.__account_number = account_name
        self.__holder_name = holder_name
        self.__balance = balance
    def display(self):
        print(f"Balance: {self.__balance}")

b1 = BankAccount()
b1.set_detail("current","kapil",23000)
b1.display()


class Car:
    def __init__(self):
        # random initialization of the instance variables
        self.__brand = "Maruti Suzuki"
        self.__model = "RZT-324"
        self.__year = 2000
    
    def setter_details(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
    
    def get_detail(self):
        return self.__dict__

c1 = Car();
c1.setter_details("Honda", "TZCF-345", 2023)
# print(c1.get_detail())


class Inventory:
    def set_detail(self, productId, name, quantity, price):
        self.__productId = productId
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def get_total_price(self):
        return self.__quantity * self.__price

p1 = Inventory()
p1.set_detail(1, "Mouse", 23, 250)
# print(f"Total Price: {p1.get_total_price()}")



class Movie:
    def setter_detail(self, name, genre, rating):
        self.__name = name
        self.__genre = genre
        self.__rating = rating
    
    def isHit(self):
        if self.__rating>8.0:
            return True
        else:
            return False
    
m1 = Movie()
m1.setter_detail("The Flying Jat", "Fun", 9.4)
# print(m1.isHit())


class ResultChecker:
    def setter_detail(self, name, mathMark, scienceMark):
        self.__name = name
        self.__mathMark = mathMark
        self.__scienceMark = scienceMark
    
    def calc_avg(self):
        return (self.__mathMark+self.__scienceMark)/2

st1 = ResultChecker()
st1.setter_detail("Kapil", 45, 67)
# print(f"Average of marks: {st1.calc_avg()}")


class Phone:
    def __init__(self):
        # random initialization of the instance variables
        self.__brand = "Vivo"
        self.__model = "Y12"
        self.__price = 22000
    
    def setter_details(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price
    
    def isAffordable(self):
        if self.__price<20000:
            return "Affordable"
        else:
            return "Unaffordable"

c1 = Phone();
c1.setter_details("samsung", "s24", 1500000)
# print(c1.isAffordable())


class Circle:
    def set_value(self, radius):
        self.__radius = radius
    
    def get_area(self):
        return self.__radius*self.__radius*3.14

area = Circle()
# area.set_value(24)
# print(area.get_area())



class Rectangle:
    def set_value(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def calc(self):
        return self.__length*self.__breadth

area = Rectangle()
area.set_value(23,44)
# print(area.calc())


    
