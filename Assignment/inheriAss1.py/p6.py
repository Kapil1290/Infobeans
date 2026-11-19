class Staff:
    def __init__(self, name, age, id):
        self.__name = name
        self.__age = age 
        self.__id = id

    def duty(self):
        pass

class Doctor(Staff):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)

    def duty(self):
        print("Check allocated patients")
        print("handle emergency cases")


class Nurse(Staff):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)

    def duty(self):
        print("Help doctor")
        print("Deal with patient family members")

class Pharmasist(Staff):
    def __init__(self,name, age, id):
        super().__init__(name, age, id)

    def duty(self):
        print("Give medicines")
        print("Check stock")

p = Pharmasist("kapil",22,101)
p.duty()

    

    