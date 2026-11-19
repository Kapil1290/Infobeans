class Person:
    def __init__(self,name,id):
        self.__name = name 
        self.__id = id 

    def __str__(self):
        return f"{self.__name}\n{self.__id}"

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name,id)
        self.__attendance = False

    def mark_attendance(self):
        self.__attendance = True

    def get_detail(self):
        print(self)

class Teacher(Person):
    def __init__(self, name, id):
        super().__init__(name,id)
    
    def take_attendance(self):
        print("taking attendance..")

    def get_detail(self):
        print(self)

t = Teacher("raam",101)
t.take_attendance()
s = Student('kapil',101)
print("="*30)
s.get_detail()
print("="*30)
t.get_detail()