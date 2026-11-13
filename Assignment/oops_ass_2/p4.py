class Student:
    def __init__(self, name, roll, marks):
        self.__name = name
        self.__roll = roll 
        self.__mark = list(marks)
        print(self.__mark)

    def total_marks(self):
        return sum(self.__mark)

    def percent_calc(self):
        percent = (sum(self.__mark)/300)*100
        if percent>90:
            print(f"You got {round(percent,2)} with grade A")
        elif percent>75:
            print(f"You got {round(percent, 2)} with grade B")
        elif percent>50:
            print(f"You got {round(percent, 2)} with grade C")
        else:
            print(f"You got {round(percent, 2)} Failed......")

s1 =Student("Kapil", 121, [77,84,90])``
print(s1.total_marks())
s1.percent_calc()