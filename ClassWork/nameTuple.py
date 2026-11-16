from collections import namedtuple 

Student = namedtuple("Student", ["name","id"])

s1 = Student("kapil",123)

print(s1.name)