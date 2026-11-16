class Student:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    
    
class Teacher:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id


class Class:
    __student = {}
    __teacher = {}
    __std_count = 0
    def add_student(self,name,id):
        Class.__student[id] = Student(name,id)
        print("Student added")
        Class.__std_count += 1

    def remove_student(self,name,id):
        if id in Class.__student:
            del Class.__student[id]
            print("Student removed")

    def add_teacher(self,name,id):
        Class.__teacher[id] = Teacher(name, id)
        print("Teacher added")

    def remove_teacher(self,name,id):
        if id in Class.__teacher:
            del Class.__teacher[id]
            print("Teacher removed")
    
    def count_class(self):
        print(Class.__std_count)
        return

c1 = Class()
c1.add_student("kapil",1)
c1.add_student("pawan",2)
c1.count_class()

    