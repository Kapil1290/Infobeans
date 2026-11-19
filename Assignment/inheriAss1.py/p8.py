class Fooditem:
    def calc_bill(self):
        pass


class Pizza(Fooditem):
    def calc_bill(self):
        each = 150
        quantity = int(input("Enter pizza quantity: "))
        print(f"Each pizza price: {each}")
        print(f"Total bill: {each*quantity}")

class Burger(Fooditem):
    def calc_bill(self):
        each = 130
        quantity = int(input("Enter burger quantity: "))
        print(f"Each burger price: {each}")
        print(f"Total bill: {each*quantity}")
        
class Sandwich(Fooditem):
    def calc_bill(self):
        each = 100
        quantity = int(input("Enter sandwich quantity: "))
        print(f"Each sandwich price: {each}")
        print(f"Total bill: {each*quantity}")


s = Sandwich()
s.calc_bill()