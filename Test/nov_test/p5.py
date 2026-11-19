class Product:
    def __init__(self, product_id, name, price, category):
        self.__id = product_id
        self.__name = name
        self.__price = price
        self.__category = category

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, obj):
        return self.__id == obj.__id

    def __str__(self):
        return f"Id: {self.__id}\nName: {self.__name}\nPrice: {self.__price}"
    
    def get_price(self):
        return self.__price

class ProductMgt:
    __product_collection = {}
    def __init__(self, product_id, name, price, category):
        if product_id in ProductMgt.__product_collection:
            print("Id already present")
            return 
        ProductMgt.__product_collection[product_id] = Product(product_id, name, price, category)

    def display_product(self):
        for i in ProductMgt.__product_collection:
            print(f"{i}: {ProductMgt.__product_collection[i]}")
            print("="*30)

    def sec_large_price(self):
        prices = []
        firMax = 0
        secMax = 0
        for product in ProductMgt.__product_collection:
            if ProductMgt.__product_collection[product].get_price()>firMax:
                firMax = secMax
                secMax = ProductMgt.__product_collection[product].get_price()
        print(secMax)

    def top_high_price_product(self):
        top = int(input("Enter top amount product: "))
        for product in ProductMgt.__product_collection:
            if ProductMgt.__product_collection[product].get_price()>top:
                print(ProductMgt.__product_collection[product])
                
        

    def average_calc(self):
        total = 0
        for product in ProductMgt.__product_collection:
            total += ProductMgt.__product_collection[product].get_price()
        print(f"Average: {total/len(ProductMgt.__product_collection)}")




p1 = ProductMgt(101, "Mouse", 600, "electrocis")
p2 = ProductMgt(102, "keyboard", 400, "electrocis")
p3 = ProductMgt(102, "keyboard", 10000, "electrois")

p1.display_product()
p1.sec_large_price()
p1.average_calc()
p1.top_high_price_product()



    