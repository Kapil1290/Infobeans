from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod 
    def salary_calc():
        pass

class HR(Employee):
    def salary_calc(self, salary):
        gst = 2.0
        return salary - ((gst/100)*salary)

class Developer(Employee):
    def salary_calc(self, salary):
        gst = 3.0
        return salary - ((gst/100)*salary)

class Tester(Employee):
    def salary_calc(self, salary):
        gst = 2.5
        return salary - ((gst/100)*salary)

t = Tester().salary_calc(12000)
print(t)
        
    

