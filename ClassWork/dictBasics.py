# t = ["apple", "ant", "cat", "cherrry"]

# result = {}
# for str in t:
#     ch = str[0]
#     if ch in result:
#         result[ch].append(str)
#     else:
#         result[ch]=[str]

# print(result)



# ordered collection, mutable type 
d1 = {
    "a":12,
    "b":33,
    "c":45
}

d1 = dict(a=23, b=44, c=33) # passed using =
print(d1)

products = [
    {
        "id":101,
        "title":"laptop",
        "price":200000
    },
    {
        "id":101,
        "title":"laptop",
        "price":200000
    },
    {
        "id":101,
        "title":"laptop",
        "price":200000
    },
    {
        "id":101,
        "title":"laptop",
        "price":200000
    }
]

list_of_id = []
for i in range(len(products)):
    list_of_id.extend(products[i].values())
print(list_of_id)

s = products[1].popitem()  # popitem() return the popped element in tuple format
print(s)
for i in products:
    print(i)


print(list(products[0].keys())) # get keys as list

print(d1.items())  # return the ans in tuple format

