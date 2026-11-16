class Bill:
    def __init__(self, id, unit):
        self.__id = id
        self.__unit = unit

    def calc_bill(self):
        rupee_per_unit = Bill.rupee_unit(self.__unit)
        surcharge = Bill.surcharge()
        amount = (surcharge/100)*self.__unit*rupee_per_unit

        total = self.__unit*rupee_per_unit+amount
        print(f"Total Bill is : {total:.2f}")
        return total

    def bill_summary(self):
        print(f"{Bill.rupee_unit(self.__unit)} per unit")
        print(f"Surcharge: {Bill.surcharge()}")
        print(f"Total : {self.calc_bill()}")

    @staticmethod
    def rupee_unit(units):
        if units>=100:
            return 8
        elif units>0 and units<100:
            return 5

    @staticmethod
    def surcharge():
        return 1.01

b1 = Bill(102, 23)
b1.calc_bill()
b1.bill_summary()

    
