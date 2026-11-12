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

