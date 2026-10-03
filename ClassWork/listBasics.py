
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(x[8])

# x.append(120)
# print(x)

x.insert(-8, 20)

# x.insert(12, 209)

# y = [12, 23, 34]

# x.extend(y)

# x[1:6:2] = ['A',"B","C"]
# print(x)

# y[0:23:2] = ['B','C']
print(x)
# x.remove(200)

# del x[1:3]
# print(x)
ans=0
for i in x:
    ans+=i
print(ans)

item = int(input("enter search eleement: - "))
s = 'element found'
result=[]
for i in range(len(result)):
    if item==x[i]:
        result.append(i)
    
for i in result:
    # if i==
    s = s+" "+str(i)
print(s)