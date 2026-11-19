class Product:
    def discount(self):
        pass

class Electrocics(Product):
    def discount(self,salary):
        print("You got 3% discount")
        print(f"Total bill : {salary-(10/100)*salary}")

class Grocery(Product):
    def discount(self,salary):
        print("You got 3% discount")
        print(f"Total bill : {salary-(3/100)*salary}")

class Clothing(Product):
    def discount(self,salary):
        print("You got 5% discount")
        print(f"Total bill : {salary-(5/100)*salary}")

c = Electrocics()
c.discount(1200)