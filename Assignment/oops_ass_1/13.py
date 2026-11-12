class Inventory1:
    def __init__(self):
        self.__inventory_items_collection = []

    def add_product(self, productId, product, quantity):
        dic = {"id": productId, "product": product, "quantity":quantity}
        self.__inventory_items_collection.append(dic)

    def remove_product(self, productId):
        for i in range(0, len(self.__inventory_items_collection)):
            if self.__inventory_items_collection[i]["id"] == productId :
                self.__inventory_items_collection.pop(i)
                print(f"Item Deleted.....id: {productId}")
                break
        else:
            print(f"No item available with id: {productId}")
    
    def display(self):
        print(self.__inventory_items_collection)

    def status_quantity(self):
        print("\n")
        for i in range(0, len(self.__inventory_items_collection)):
            print(f"{self.__inventory_items_collection[i]["product"]} : {self.__inventory_items_collection[i]["quantity"]}")
        

i1 = Inventory1()
i1.add_product(112, "Mouse", 30)
i1.add_product(233, "Monitor", 33)
# i1.display()
# i1.remove_product(112)
# i1.status_quantity()