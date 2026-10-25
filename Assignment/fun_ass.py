# 1
'''
def add(a=0, b=0):
    return a+b

def substract(a,b):
    return a-b

def divide(a,b):
    return a//b 
 
def multi(a,b):
    return a*b 

def modulo(a,b):
    return a%b

while True:
    print("--------------------Menu-----------------------")
    print("1 for Add number")
    print("2 for Substract number ")
    print("3 for Divide number")
    print("4 for Multiply number")
    print("5 for exit")
    print("6 for Modulo calc")
    
    choice = input('enter choice--------')
    if choice == "5":
        break
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    

    if choice=="1":
        print(f"Addition is: {add(a,b)}")
    elif choice=="2":
        print(f"Substraction is: {substract(a,b)}")
    elif choice=="3":
        if not b:
            print("Infinity")
        else:
            print(f"Divition is: {divide(a,b)}")
    elif choice=="4":
        print(f"Multiplication is: {multi(a,b)}")
    elif choice=="6":
        print(f"Modulo is: {modulo(a,b)}")
    else:
        print(f"Invalid choice!! Choose again---------")




# 2

def calculate_total(marks):
    return sum(marks) 
def calculate_percentage(marks):
    total = calculate_total(marks)
    return (total//5)
def calculate_grade(marks):
    percent = calculate_percentage(marks)
    print(percent)
    if 90<=percent<=100:
        return "Grade A"
    elif 65<=percent<=89:
        return "Grade B"
    elif 54<=percent<=64:
        return "Grade C"
    elif 44<=percent<=53:
        return "Grade D"
    else:
        return "Grade E (Poor Performance)"


print("Enter the marks of your 5 subjects")
i=0
marks = []
while i<5:
    marks.append(int(input()))
    i+=1
print(f"Total marks: {calculate_total(marks)}")
print(f"Percentage: {calculate_percentage(marks)}%")
print(f"Grade: {calculate_grade(marks)}")



# 3

amount = 50000
def display_amt():
    print(f"Current balance is: {amount}")
    return 

def deposit(amt):
    global amount
    amount += amt
    return f"Deposit {amt} done. Current balance {amount}"

def withdraw(amt):
    global amount
    if amt > amount:
        return f"Insufficient Balance!!!"
    
    amount -= amt
    return f"Withdraw done. Current balance: {amount}"

attempt = 3
secret = "123"
while attempt!=0:
    if attempt<=2:
        print(f"enter password (Remaining attempt: {attempt}): ")
        password = input()
    else:
        print("enter password: ")
        password = input()
    if password==secret:
        print("Password Matched.......")
        break
    attempt-=1

while True:
    print("--------------------Menu-----------------------")
    print("1 for Display Amount ")
    print("2 for Withdraw amount ")
    print("3 for Deposit amount")
    print("5 for exit")

    choice = input()
    if choice == "5":
        break
    
    if choice=="1":
        display_amt()
    elif choice=="2":
        amt = int(input("Enter Amount you want: "))
        print(withdraw(amt))
    elif choice=="3":
        amt = int(input("Enter Amount for deposit: "))
        print(deposit(amt))




# 4
cart_price = 0
bucket = {}
while True:
    
    items_price = {
        "pyramid":200,
        "maggi":100,
        "papad":50,
        "masala":250
    }
    print("--------------------Welcome to GiggaMart-----------------------")
    print(f"1 for Aaloo pyramid price:{items_price["pyramid"]}")
    print(f"2 for Maggi-manchurian price:{items_price["maggi"]}")
    print(f"3 for chatapata papad price:{items_price["papad"]}")
    print(f"4 for curry papad price:{items_price["masala"]}")
    print("5 for exit")

    choice = input()
    
    if choice=="5":
        print("Thank Your!")
        
        if cart_price:
            print("------------Bill-------------------")
            print(f"Items\tquatity\tprice")
            for key,value in bucket.items():
                print(f"{key}\t{value}\t {items_price[key]*value}")


            if 3000<=cart_price>=5000:
                print(f"1.8% GST added")
                gst = 4/100*(cart_price)
                print(f"Hurrah you earn 5% discount\nTotal : {(cart_price-((5/100)*cart_price)+gst)}")
            elif cart_price>5000:

                print(f"4% GST added")
                gst = 4/100*(cart_price)
                print(f"Hurrah you earn 6.5% discount\nTotal : {(cart_price-((6.5/100)*cart_price)+gst)}")
            else:
                print(f"Total amount: {cart_price}")
        break
    
    if choice=="1":
        cart_price+=items_price["pyramid"]
        bucket["pyramid"] = bucket.get("pyramid",0)+1
        print(f"Running Amount till now: {cart_price}")
    elif choice=="2":
        cart_price+=items_price["maggi"]
        bucket["maggi"] = bucket.get("maggi",0)+1
        print(f"Running Amount till now: {cart_price}")
    elif choice=="3":
        cart_price+=items_price["papad"]
        bucket["papad"] = bucket.get("papad",0)+1
        print(f"Running Amount till now: {cart_price}")
    elif choice=="4":
        cart_price+=items_price["masala"]
        bucket["masala"] = bucket.get("masala",0)+1
        print(f"Running Amount till now: {cart_price}")
    else:
        print("Invalid Menu!!!!!!")
    
'''


# 5

product_list_piece = {
    "mouse":{
        "price":350,
        "quatity_available":34
    },
    "keyboard":{
        "price":760,
        "quatity_available":44
    },
    "monitor":{
        "price":7000,
        "quatity_available":8
    },
    "power":{
        "price":7000,
        "quatity_available":8
    },
    "cpubox":{
        "price":900,
        "quatity_available":10
    },
    "battery":{
        "price":7500,
        "quatity_available":4
    }
}

products=[]
for key in product_list_piece.keys():
    products.append(key)
print(products)
cart = {}

while True:
    print("----------------Welcome--------------------")
    ch = 1
    for key,value in product_list_piece.items():
        print(f"press: {ch} {key}        ", end=" ")
        print(f"{value["price"]} /-")
        ch+=1
    
    choice = input()
    if choice=="1":
        need = int(input("Enter Quatity: "))
        
        if product_list_piece[products[int(choice)-1]]["quatity_available"]>=need:
            cart[products[int(choice)-1]]=cart.get(products[int(choice)-1], 0)+1
            product_list_piece[products[int(choice)-1]]["quatity_available"]-=need
        else:
            print(f"{products[int(choice)-1]} Insufficient")
    
    elif choice=="2":
        need = int(input("Enter Quatity: "))

        if product_list_piece[products[int(choice)-1]]["quatity_available"]>=need:
            cart[products[int(choice)-1]]=cart.get(products[int(choice)-1], 0)+1
            product_list_piece[products[int(choice)-1]]["quatity_available"]-=need
        else:
            print(f"{products[int(choice)-1]} Insufficient")
    break





