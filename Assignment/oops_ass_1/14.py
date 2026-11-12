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
