# n = int(input("enter number n:- "))
i=1
# for _ in range(n):
#     print(i)
#     i+=2

# for i in range(1, n+1):
#     print(i*i)

a=1
b=2
# print(a,end=" ")
# print(b,end=" ")
# for _ in range(n):
#     print(a,end="  ")
#     c=a*b 
#     a=b 
#     b = c 

# for i in range(65, 91):
#     print(chr(i+32), end=" ")

# sum = 0
# for i in range(1,n+1):
#     sum += 1/i
# print(int(sum))








print(ord("1"))


def fake(a):
    a.append(34)
a = [3,2,3]
fake(a)
print(a)

# s = "kapil"
# t = s.join("prajapat")
# print(t)

# print(s.replace("ka",""))

# print("\n")

# def add(item, items=[]):
    
#     items.append(item)
#     return items
# print(add(1))
# print(add(2))
# print(add(3))



s = "ram ramji roohoram ramrram ram is my friramjikorammji"
inp = "ram"
idx = 0
res = ""
count=0
for i in range(0, len(s)):
    if s[i]==inp[idx]:
        res += s[i]
        idx+=1
    else:
        res = ""
        idx=0
        if s[i]==inp[idx]:
            res += s[i]
            idx+=1  
    if res==inp:
        count+=1
        res = ""
        idx=0
# if res==inp:
#     count+=1
print(count)



# def my_decorator(func):  # 'func' is the function object, not its signature
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def add(x, y):
#     return x + y

# print(add(2,3))





a = {"name":"kapil"}
b = a.copy()
print(b)
b["name"]="hariom"
print(b)
print(a)


print(345/500*100)

print(34.3444444>32)


s = "()))(("

# i=0
# count=0
# while i<len(s)-1:
#     if s[i]=='(':
#         if s[i+1]==')':
#             i+=2
#         else:
#             count+=1
#             i+=1
#     else:
#         count+=1
#         i+=1
# print(count)
    
i=0
count=0
for i in range(0,len(s)-1):
    if s[i]=='(' and s[i+1]==')':
        count+=2

print(len(s)-count)



a = ['a', 'b', 'c', 'd']
for i, item in enumerate(a):
    print(i, item)


