class Cart:
    total_cart = 0
    def __init__(self, name, total_bill):
        self.__name = name
        self.__total_price = total_bill
        self.__product_list = []

        Cart.total_cart += 1
        print(f"Total cart: {Cart.total_cart}")
    
    def add(self, product, id, price):
        coll = {"product": product, "id": id, "price": price}
        self.__product_list.append(coll)
        self.__total_price += price
        print("Item added")
    
    def remove(self, id):
        for i in range(0, len(self.__product_list)):
            if self.__product_list[i]["id"] == id:
                self.__product_list.remove(i)
                return
        else:
            print(f"product not found with id {id}")

    def final_bill(self):
        return Cart.after_discount(self.__total_price)

    @staticmethod
    def after_discount(amount):
        if amount <= 5000:
            return amount - ((5/100)*amount) 
        else:
            return amount - ((10/100)*amount)

p1 = Cart("kapil",0)
p1.add("bicuit", 111, 200)
p1.add("jelly",222, 200)
p2 = Cart("hayor",0)
print(Cart.total_cart)
print(p1.final_bill())