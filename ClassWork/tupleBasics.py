# tuple is immutable

t = (12,22,3,2,1,44,5,2,3)





products = [
    {"id":100, "title":"laptop", "price":200000},
    {"id": 101, "title":"mouse", "price":2000},
    {"id":102, "title":"cpu", "price": 2300}
]

for key in products:
    print(f"{key["id"]}\t{key["title"]}\t{key["price"]}")


a = 12
b = 22
print(id(a))
a = 13
print(id(a))



