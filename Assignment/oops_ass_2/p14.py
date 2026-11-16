class Restorant:
    __menu = {"chhola tikki":100,"aloo paratha":120,"poha":70,"samosa":90,"coffee":150,"tea":60}

    def __init__(self,table_number,cart):
        self.__table_number = table_number
        self.__cart = cart
        self.__price = 0
        for item in self.__cart:
            if item in Restorant.__menu:
                self.__price += Restorant.__menu[item]

    def add_item(self, item):
        if item in Restorant.__menu:
            self.__cart.append(item)
            self.__price += Restorant.__menu[item]
        else:
            print("item not available")

    def remove_item(self, item):
        if item in self.__cart:
            self.__cart.remove(item)
        else:
            print("item not present")

    @staticmethod
    def service_tax():
        return 200

    def bill(self):
        print("="*20)
        print(f"Total Item : {self.__cart}")
        print(f"Price: {self.__price}")
        print(f"Service tax: {Restorant.service_tax()}")
        print(f"Total Bill: {self.__price+Restorant.service_tax()}")

r1 = Restorant(1, ["aloo paratha","samosa"])
r1.bill()