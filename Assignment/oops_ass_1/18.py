# 14
class Restorant:
    def __init__(self):
        self.__menu = []

    def items_details(self, item, price, rating):

        d = {
            "item": item,
            "price": price,
            "rating": rating
        }
        self.__menu.append(d)
        print("item added")

    def remove_item(self, item):
        for i in range(0, len(self.__menu)) :
           if self.__menu[i]["item"] == item:
            self.__menu.pop(i)
            print("item removed")
            break
        else:
            print("item not found.....")

    def get_average(self):
        sum = 0
        for i in range(0, len(self.__menu)):
            sum += self.__menu[i]["rating"] 
        print(f"Average rating is: {sum//len(self.__menu)}")


r1 = Restorant()
# r1.items_details("Vadapav", 80, 7)
# r1.items_details("Aloo pyramid", 120, 8)
# r1.get_average()