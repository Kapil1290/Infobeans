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