class Employee:
    def __init__(self, name, salary, mmyy, current_mmyy):
        month = 0
        year = 0
        self.__name = name
        self.__salary = salary
        year = int(current_mmyy[3:]) - int(mmyy[3:])
        month = 12 - int(mmyy[0:2])
        month += int(current_mmyy[0:2])
        year1 = int(mmyy[3:5])+1
        year2 = int(current_mmyy[3:5])-1
        year = (year2 - year1)*12
        month = (month+year)*salary
        self.__total_salary = month

    def calc_salary(self):
        print(f"Salary: {self.__total_salary}")
    
em1 = Employee("kapil",23000, "02-04", "05-26")
em1.calc_salary()