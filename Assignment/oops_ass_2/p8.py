class Product:
    __product = {}
    def __init__(self, id, product, price, quantity):
        self.__id = id
        self.__product = product
        self.__price = price
        self.__quantity = quantity

        Product.__product[id] = {"id":id, "product":product, "price": price, "quantity":quantity}

    def add_stock(self, id, quantity):
        if id in Product.__product:
            Product.__product[id]["quantity"] += quantity
            print("stock added")
            return
        else:
            print("product not found...")
            return

    def purchase(self, id, quantity):
        if id in Product.__product and Product.__product[id]["quantity"] >= quantity:
            Product.__product[id]["quantity"] -= quantity
            print("purchased..")
            return
        else:
            print("stock is low...")
            return 

p1 = Product(101, "mouse", 1200, 20)
p1.purchase(101, 10)
p1.purchase(101, 10)
p1.add_stock(101, 10)
p1.purchase(101,10)
        