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


class Account:
    def __init__(self):
        self.__balance = 1.0
    
    def setter_details(self, holder, accountNum, amount):
        self.__holder = holder
        self.__accountNum = accountNum
        self.__balance = amount
    
    def get_detail(self):
        return self.__dict__

cust1 = Account();
cust1.setter_details("Kapil", "4990189945876000025", 23000)
# print(cust1.get_detail())



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




# 1
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

# 2
class Dog:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed
    
    def set_breed(self, breed):
        self.__breed = breed

    def get_dog(self):
        print(f"DogName: {self.__name}\nBreed: {self.__breed}")
    
d1 = Dog("Puppy", "Labra")
d1.set_breed("Golden") # changing the breed
# d1.get_dog()

# 3
class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
    
    def get_area(self):
        print(f"Areae is: {self.__length*self.__breadth}")

r1 = Rectangle(20,30)
# r1.get_area()

# 4
class Circle2:
    def __init__(self, radius):
        self.__radius = radius
    
    def get_circum(self):
        print(f"Circumstance: {3.14*self.__radius}")

c1 = Circle2(23)
# c1.get_circum()


# 5
class Book1:
    def __init__(self):
        self.__collection = []
    

    def add(self, title, author, isbn):
        self.__title= title
        self.__author = author
        self.__isbn = isbn
        self.__collection.append({"title":self.__title,"author":self.__author,"isbn":self.__isbn})

    def remove(self, isbn):
        for i in range(0, len(self.__collection)):
            if self.__collection[i]["isbn"]==isbn:
                self.__collection.pop(i)
                print(f"Book deleted with isbn: {isbn}")
                break
        else:
            print(f"Book not found with isbn: {isbn}")

    def current_collection(self):
        print(f"{self.__collection}")

b1 = Book1()
b1.add("The new aura", "john doe", 2132)
b1.add("Time is gold", "ratibi", 2354)
b1.add("Time is gold", "ratibi", 5255)
b1.add("The Real world", "micheal", 7658)
# b1.current_collection()
# b1.remove(7658)
# b1.current_collection()

# 5
class Bank:
    account_lib = []
    def add_account(self,account_detail):
        Bank.account_lib.append(account_detail)

    def remove(self, accNo):
        for i in range(0, len(Bank.account_lib)):
            if Bank.obj_lib[i]["_Account__accountNum"]==accNo:
                Bank.obj_lib.pop(i)
                break
        else:
            print(f"No acc found")
    def get_record(self):
        print(Bank.account_lib)



class Account:
    def __init__(self, name, age, account_number, account_type):
        self.__name = name
        self.__age = age
        self.__amount = 0
        self.__account_number = account_number
        self.__account_type = account_type

    def deposit(self, amt):
        self.__amount += amt
        print(f"Amount successfully deposited {self.__amount}")  

    def withdraw(self, amt):
        if self.__amount>=amt:
            self.__amount -= amt
            print(f"Amount successfully withdraw: {amt}")
        else:
            print(f"No sufficient amount.....")
    
    def get_details(self):
        dic = {
            "name": self.__name, "age":self.__age, "amount":self.__amount, "account_number":self.__account_number, "type":self.__account_type
        }
        return dic

a1 = Account("Kapil", 23, "2339847555", "saving")
a2 = Account("om", 22, "284995768", "current")
# a1.deposit(23000)
# a2.deposit(2000)  
# detail_saving = a1.get_details()
# detail_current = a2.get_details()
# a2.withdraw(23000)

# saving = Bank()
# current = Bank()
# current.add_account(detail_current)
# saving.add_account(detail_saving)
# current.get_record()



# 6
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


# 7
class EMP:
    def __init__(self, name, salary, title):
        self.__name = name
        self.__salary = salary
        self.__title = title
    
    def set_salary(self, salary):
        self.__salary = salary
    def get_info(self):
        print(f"Name: {self.__name}\nSalary: {self.__salary}\ntitle: {self.__title}")
    

e1 = EMP("kapil", 23000, "Hr")
e1.set_salary(20000)
# e1.get_info()


# 8
class Student:
    def __init__(self, name, grade, *courses):
        self.__name = name
        self.__grade = grade
        self.__course = [string.upper() for string in list(courses)]
        
    
    def add(self, course):
        self.__course.append(course.upper())
    
    def remove(self, course):
        course = course.upper()
        for string in self.__course:
            if string == course:
                self.__course.remove(course)
        else:
            print(f"Course not found....")
    
    def __str__(self):
        return f"Name: {self.__name}\nGrade: {self.__grade}\nCourses: {self.__course}"

std1 = Student("kapil", "A", "Math","English","Sports","Biology")
# std1.add("History")
# std1.remove("sports")
# print(std1)


# 9
class Airoplane:
    def __init__(self, flight_number, destination, depart_time):
        self.__flight_number = flight_number
        self.__destination = destination
        self.__depart_time = depart_time

    def check_status(self):
        print(f"Flight Details\nFlight Number: {self.__flight_number}\nDestination: {self.__destination}\nDepartTime: {self.__depart_time}")

a1 = Airoplane(233, "Hydrabad", "12:30 PM")
a2 = Airoplane(112, "London", "11:00 AM")
# a1.check_status()
# a2.check_status()

#10
class Inventory1:
    def __init__(self):
        self.__inventory_items_collection = []

    def add_product(self, productId, product, quantity):
        dic = {"id": productId, "product": product, "quantity":quantity}
        self.__inventory_items_collection.append(dic)

    def remove_product(self, productId):
        for i in range(0, len(self.__inventory_items_collection)):
            if self.__inventory_items_collection[i]["id"] == productId :
                self.__inventory_items_collection.pop(i)
                print(f"Item Deleted.....id: {productId}")
                break
        else:
            print(f"No item available with id: {productId}")
    
    def display(self):
        print(self.__inventory_items_collection)

    def status_quantity(self):
        print("\n")
        for i in range(0, len(self.__inventory_items_collection)):
            print(f"{self.__inventory_items_collection[i]["product"]} : {self.__inventory_items_collection[i]["quantity"]}")
        

i1 = Inventory1()
i1.add_product(112, "Mouse", 30)
i1.add_product(233, "Monitor", 33)
# i1.display()
# i1.remove_product(112)
# i1.status_quantity()

#11
class School:
    def __init__(self,class_name):
        self.__class_name = class_name
        self.__teachers = []
        self.__students = []

    def add_student(self, name, rollno):
        detail = {
            "name":name, 
            "roll": rollno
        }
        self.__students.append(detail)
        print(f"Student added...id: {rollno}")
    
    def add_teacher(self, name, teacher_id):
        detail = {
            "name":name, 
            "id": teacher_id
        }
        self.__teachers.append(detail)
        print(f"Teacher added...id: {teacher_id}")
    
    def remove_student(self, rollno):
        for i in range(0, len(self.__students)):
            if self.__students[i]["roll"] == rollno:
                self.__students.pop(i)
                print("Student removed.....")
                break
        else:
            print(f"Student not found...")

    def remove_teacher(self, id):
        for i in range(0, len(self.__teachers)):
            if self.__teachers[i]["id"] == id:
                self.__teachers.pop(i)
                print("Teacher removed.....")
                break
        else:
            print(f"Teacher not found...")
        
    def get_class(self):
        print(f"\nClass: {self.__class_name}\nStudents are: {self.__students}\nTeachers are: {self.__teachers}")
        return

c1 = School("2nd")
# c1.add_student("kapil", 101)
# c1.add_student("girdhari", 102)
# c1.add_teacher("Sitaram", 101)
# c1.add_teacher("Siya", 102)
# c1.remove_student(101)
# c1.get_class()

c2 = School("3rd")
# c2.add_student("hemant", 103)
# c2.add_student("divya", 104)
# c2.add_teacher("ram", 105)
# c2.add_teacher("sonu", 105)
# c2.remove_student(103)
# c1.get_class()


#12
class MusicLibrary:
    def __init__(self):
        self.__library = []
    
    def add_music(self, title, singer):
        music = { "title": title, "singer": singer }
        self.__library.append(music)
        print("Music added.....")  
    
    def play_random(self):
        for i in range(0, len(self.__library)):
            print(f"Playing: {self.__library[0]["title"]}.....")
            break
        return

m1 = MusicLibrary()
# m1.add_music("teri kasam ho....", "Aham")
# m1.add_music("sitaram sitaram", "gopinath")
# m1.play_random()


#13
class Movie1:
    def __init__(self, title, director, *actors):
        self.__title = title
        self.__actor = list(actors)
        self.__director = director
        self.__review = []

    def add_review(self, *review):
        self.__review.extend(review)
        print(f"Review added.....review: {review}")
    
    def remove_review(self):
        self.__review.pop()
        print(f"review removed.....review: {self.__review}")

m1 = Movie1("rebel", "kunika", "amitabh", "sahruk","sunil")
# m1.add_review(4,2,3,5,4)
# m1.remove_review()


# 14
class Restorant:
    def __init__(self):
        self.__menu = []

    def items_details(self, item, price, rating):

        d = {
            "item": item,
            "price": price,
            "rating": rating
        }
        self.__menu.append(d)
        print("item added")

    def remove_item(self, item):
        for i in range(0, len(self.__menu)) :
           if self.__menu[i]["item"] == item:
            self.__menu.pop(i)
            print("item removed")
            break
        else:
            print("item not found.....")

    def get_average(self):
        sum = 0
        for i in range(0, len(self.__menu)):
            sum += self.__menu[i]["rating"] 
        print(f"Average rating is: {sum//len(self.__menu)}")


r1 = Restorant()
# r1.items_details("Vadapav", 80, 7)
# r1.items_details("Aloo pyramid", 120, 8)
# r1.get_average()






#19
class Flight:
    def __init__(self, flight_id, destination, price):
        self.flight_id = flight_id
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"Flight Details: {self.flight_id}\nDestination: {self.destination}\nPrice: {self.price}"

    def __repr__(self):
        return self.__str__()

class Hotel:
    def __init__(self, hotel_id, name, price_per_night, city):
        self.hotel_id = hotel_id
        self.name = name
        self.price_per_night = price_per_night
        self.city = city

    def __str__(self):
        return f"Hotel Details: {self.hotel_id}\nCity: {self.city}\nPrice_per_day: {self.price_per_night}"

    def __repr__(self):
        return self.__str__()

class ReservationSystem:
    def __init__(self):
        self.flights = [
            Flight("B82", "Hydrabad", 10000),
            Flight("A23", "Mumbai", 50000),
            Flight("S32", "Delhi", 20000),
            Flight("V33", "Pune", 20000)
        ]
        self.hotels = [
            Hotel("BH12","Raja bhoj", 1200, "Jaipur"),
            Hotel("BA52","Yaswantji hotel", 5000, "Pune"),
            Hotel("BD42","Raja bhoj", 2500, "Mumbai")
        ]
        self.bookings = {}

    def search_flight(self, destination):
        return [f for f in self.flights if f.destination.lower() == destination.lower()]

    def search_hotel(self, city):
        return [ h for h in self.hotels if h.city.lower() == city.lower()]
    

    def book_flight(self, flight_id):
        for f in self.flights:
            if f.flight_id.lower() == flight_id.lower():
                print(f"FLIGHT SUCCESSFULLY BOOKED.")
                self.bookings[flight_id] = f
                break
        else:
            print(f"Flight not found.....")


    def book_hotel(self, hotel_id):
        for h in self.hotels:
            if h.hotel_id.lower() == hotel_id.lower():
                print(f"FLIGHT SUCCESSFULLY BOOKED.")
                self.bookings[hotel_id] = h
                break
        else:
            print(f"Hotel not found.....")

res = ReservationSystem()
data = res.search_flight("Pune")
# print(res.search_hotel("Pune"))

# res.book_flight("33")
# res.book_hotel("dfdf")
# print(data)




    
