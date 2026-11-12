class Employee:
    total_count=0
    def __init__(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary
        Employee.total_count+=1
    
    def total_employee(self):
        print(f"{Employee.total_count}")
    
    def emp_detail(self):
        print(f"Name: {self.__name}\nDepartment: {self.__department}\nSalary: {self.__salary}")
    
    def inc_salary(self, percent):
        amt = (percent/100)*self.__salary
        self.__salary += amt
    

e1 = Employee("kapil","Sales",12000)
e3 = Employee("sitara", "hr", 20000)
e2 = Employee("hari", "developer", 10000)
e1.total_employee()
e2.inc_salary(50)
e2.emp_detail()




    