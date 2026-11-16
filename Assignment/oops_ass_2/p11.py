class Ecommerce:
    __discount_rate = {"grocery":12, "electronic":22, "stationary":12,"medicine":10}
    def __init__(self, product, price, category):
        self.__product = product
        self.__price = price
        self.__category = category.lower() 
        self.__final_amt = price

    def category_discount(self, category):
        category = category.lower()
        if self.__final_amt:
            self.__final_amt -= (Ecommerce.__discount_rate[category]/100)*self.__final_amt
            gst = Ecommerce.apply_gst(self.__final_amt)
            self.__final_amt+=gst

    @staticmethod
    def apply_gst(amt):
        if 5000>amt<=10000:
            return (5/100)*amt
        elif amt>10000:
            return (9/100)*amt
        elif amt < 5000:
           return (2/100)*amt

    def display_price(self):
        print(f"Final price : {self.__final_amt:.2f}")
        return

a1 = Ecommerce("refine oil",120,"grocery")
a1.category_discount("Grocery")
a1.display_price()
