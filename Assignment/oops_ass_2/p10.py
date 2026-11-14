class Employee:
    def __init__(self, name, salary, id):
        self.__name = name
        self.__salary = salary
        self.__id = id

    def __eq__(self, other):    # 
        print("eq")
        return self.__id == other.__id

    def __str__(self):
        return f"{self.__name}\n{self.__salary}\n{self.__id}"

class Department:
    __employees = []
    def __init__(self, department_name):
        self.__department_name = department_name

    def add_employee(self, name, salary, id):

        obj = Employee(name, salary, id)
        if obj in Department.__employees:    # here call the eq again and again
            print(f"Id {id} already present")
        else:
            Department.__employees.append(obj)

    def get_all_employee(self):
        for i in range(0, len(Department.__employees)):
            print(Department.__employees[i])
            print("-"*30)

d1 = Department("Hr")
d2 = Department("Devops")
d1.add_employee("kapil",120000, 101)
d2.add_employee("digvijay",400000, 101)
d1.get_all_employee()
