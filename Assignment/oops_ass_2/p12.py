class Car:
    def __init__(self, number, model, price_per_day, available_status=True):
        self.__number = number
        self.__model = model
        self.__price = price_per_day
        self.__status = available_status

    def get_status(self):
        return self.__status

    def set_status(self):
        self.__status = False
    
    def get_price(self):
        return self.__price


class rental:
    __showroom = {}
    def add_car(self,number, model, price_per_day, available_status=True):
        if number not in rental.__showroom:
            rental.__showroom[number] = Car(number, model, price_per_day, available_status)
        else:
            print("Car already available")

    def get_car(self, number):

        if number in rental.__showroom:
            if rental.__showroom[number].get_status():
                rental.__showroom[number].set_status()
                print("car boooked...")
            else:
                print("car not available...")
        else:
            print(f"No car available with number: {number}")

    def return_car(self, number):
        if number in rental.__showroom:
            if not rental.__showroom[number].get_status():
                rental.__showroom[number].__status = True
        else:
            print(f"We don't have car with number: {number}")

    def calc_amt(self, day, number):
        if number in rental.__showroom:
            print(f"Total amount is: {day*rental.__showroom[number].get_price()}")
        return

c1 = rental()
c1.add_car("MP02FF2333",2023,700)
c1.add_car("OD23ER7485",2004,1200)
c1.get_car("OD23ER3485")
c1.get_car("OD23ER7485")
c1.calc_amt(2,"OD23ER7485")
