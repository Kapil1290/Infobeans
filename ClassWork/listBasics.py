
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
# for i in x:
#     ans+=i
# print(ans)

# item = int(input("enter search eleement: - "))
# s = 'element found'
# result=[]
# for i in range(len(result)):
#     if item==x[i]:
#         result.append(i)
    
# for i in result:
#     # if i==
#     s = s+" "+str(i)
# print(s)




list1 = [1,2,3,4,5]
list2 = [1,2,4,4,5]
# check the sum of elements in the list 
print(list1<=list2)

list1 = list1*list2
print(list1)


li = [
    [1,2,3,4],
    [4,3,2,1],
    [3,2,2,1],
    [9,0,8,0]
]

for i in range(len(li)):
    for j in range(len(li[i])):
        if i==j:
            print(li[i][j])

for row in li:
    for ele in row:
        print(ele, end=" ")


a = [0]*3
print(a)
a = [[0,0,0]*3]
b = [[]]*3  # it multiply inside one level
print(a)
print(b)


t = (23,33)
print(type(t))
a,b = (12, 22)
print(f"{a} and {b}")


x,y,z = (12,23,34)
print(f"{x}, {y}, {z} {type(x)}")

m, *n, o = (23,22,4,5,3,2,9,0,89)
print(f"{m} {n} {o}")

#we can't replace the list inside the tuple 
# we can edit the list inside the tuple 