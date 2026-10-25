
#2 and 26
'''
demolist = [2,3,4,5,0,43,54,23,84]
max = -111111111111
min = 1000000000000
for i in demolist:
    if max<i:
        max=i 
    if min>i:
        min=i 
print(f"max is {max} and min is {min}")


#3 and 25
demolist = [2,3,4,5,12,43,54,23,44]
low = 0
high = len(demolist)-1
print(demolist)
while(low<high):
    temp = demolist[low]
    demolist[low] = demolist[high]
    demolist[high] = temp
    low+=1
    high-=1
print(demolist)


#4
demolist = [45,34,12,43,54,23,44]
for i in range(0, len(demolist)):
    for j in range(i+1, len(demolist)):
        if (demolist[i]>demolist[j]):
            temp = demolist[i]
            demolist[i] = demolist[j]
            demolist[j] = temp

print(demolist)


#5
demolist = [2,3,4,5,12,43,54,23,44]
k = int(input("value of k: "))
demolist.sort()
print(f"kth largest element is: {demolist[-k]}")
print(f"kth smallest element is: {demolist[k-1]}")


#5
arr = [2,33,2,3,2,4,2,2]
n = int(input("enter number that you want to find occurance:- "))
count=0
for i in arr:
    if i==n:
        count+=1

print(f"Occurance of {n} is {count} in the list")


#6
arr = [0,2,1,0,2,1,2,0]
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i]>arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(arr)

#7
arr = [1,2,3,7,5]
sum = int(input("enter target sum :  "))
p1 = 0
p2 = 1
ans = arr[p1]
ans += arr[p2]
while(p2<len(arr)):
    
    if ans==sum:
        print(f"index are {p1}---{p2}")
        break
    if ans<sum:
        p2+=1
        ans += arr[p2]
    elif ans>sum:
        ans -= arr[p1]
        p1-=1


# 8
arr = [1, -3, 2, -7, -5, 11, 6 ]
low = 0
high = len(arr)-1
pos = []
neg = []
for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
arr = pos+neg
print(arr)


#9
a = [5,8,9,12,13]
b = [2,3,5,8,13,14,22]
i=0
j=0
union=[]
while i<len(a) and j<len(b):
    if a[i]==b[j]:
        if not union or union[-1]!=a[i]:
            union.append(a[i])
        i+=1
        j+=1
    elif a[i]<b[j]:
        if not union or union[-1]!=a[i]:
            union.append(a[i])
            i+=1
    else:
        if not union or union[-1]!=b[j]:
            union.append(b[j])
            j+=1

while 
print(union)



#10
arr = [1,2,3,4,5]
previous = arr[len(arr)-1]

for i in range(len(arr)-2, -1, -1):
    arr[i+1] = arr[i]
arr[0] = previous
print(arr)


#11
sum = int(input("enter sum for target: "))
arr = [2, 3, 4, 6, 5, 4, 4, 1, 2, 1]
count=0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i]+arr[j])==sum:
            count+=1
print(count)



#12
arr1 = [1,2,3,34,45,50, 40, 20]
arr2 = [7,12,23,50,60,20]
arr3 = [4, 18,17,34,50, 20, 30]
inter=[]
i=0
j=0
k=0
while i<len(arr1) and j<len(arr2) and k<len(arr3):
    if arr1[i]==arr2[j]==arr3[k]:
        inter.append(arr1[i])
        i+=1
        j+=1
        k+=1
    elif arr1[i]<arr2[j]:
        i+=1
    elif arr2[j]<arr3[k]:
        j+=1
    else:
        k+=1
print(inter)


#13
arr = [2,4,5,2,7,6]
s = set()
result=None
for i in range(len(arr)-1, -1, -1):
    if arr[i] in s:
        result=arr[i] 
        break
    s.add(arr[i])
if result:
    print("result is ", result)
else:
    print("not present")
    

#14
arr = [-1,2,-1,3,2]

for i in range(0, len(arr)-1):
    flag = 0
    for j in range(0, len(arr)):
        if j!=i:
            if arr[i]==arr[j]:
             
                flag=1
                break
    if flag==0:
        print(i) 
        break
   


#15
arr=[1,0,0,1,0,0,1]
zero=0
one=0
count=0
for i in range(len(arr)-1):
    if arr[i]==0:
        zero+=1
    else:
        one+=1
    for j in range(i+1, len(arr)):
        if arr[j]==0:
            zero+=1
        else:
            one+=1
        
        if one==zero:
            count+=1
    zero=0
    one=0
print(f"Total pairs of 0s and 1s :-  {count}")


#16
arr=[9, 4, -2, -1, 5, 0, -5, -3, 2]
newList = []
count=0
for i in range(len(arr)):
    if arr[i]>=0:
        newList.append(arr[i])
    else:
        count+=1
i=0
idx=1
while i<len(arr):
    if arr[i]<0:
        newList.insert(idx, arr[i])
        idx+=2
    i+=1
print(newList)


#17 
arr = [4,3,-3,1,0]
flag=0
value=0
for i in range(len(arr)-1):
    value+=arr[i]
    for j in range(i+1, len(arr)):
        value+=arr[j]
        if value==0:
            flag=1
            break
    value=0
if flag==0:
    print("No")
else:
    print("Yes")


#18
arr=[1,2,3,2,5]
maxSum = -111111111
for i in range(len(arr)-1):
    value += arr[i]
    for j in range(i+1, len(arr)):
        value+=arr[j]
        if value > maxSum:
            maxSum = value
    value=0
print(f"Max subarray is:- {maxSum}")


#19
arr=[6,-3,-10,0,2]
maxSum = 1
value=1
for i in range(len(arr)-1):
    value *= arr[i]
    for j in range(i+1, len(arr)):
        value*=arr[j]
        if value > maxSum:
            maxSum = value
    value=1
print(f"Max subarray is:- {maxSum}")


#20
arr = [2,3,1,5,9]
arr.sort()
count=1
for i in range(len(arr)-1):
    if arr[i]+1==arr[i+1]:
        count+=1

print(f"Contigous SubSeq :-  {count}")
'''

#21
arr= [8,3,1,2]
maxSum = -1111111
value = 0
for i in range(len(arr)):
    value += arr[i]*i
    if value>maxSum:
        maxSum=value
print(maxSum)
maxSum=0
i=0
x=0
while i<len(arr):
    j=i+1
    while j<=len(arr):
        if j==len(arr):
            j=0
        if j==i:
            value+=arr[j]*x
            break
        
        value += arr[j]*x
        if value > maxSum:
            maxSum=value
        
        j+=1
        x+=1
    i+=1
print(maxSum)


#22
arr = [1,4,5,2,7,8]
arr.sort()
print(f"Nearest lesser is {arr[0]} \nNearest Greater is {arr[len(arr)-1]}")



#23
arr = [23,34,44,56,66,78]
sum = 0
for i in arr:
    sum += i 
print(f"Sum of array is {sum} \nAverage is {(sum)/len(arr)}")

#24
arr = [23,34,44,56,66,78]
tem = arr[len(arr)-1]
arr[len(arr)-1] = arr[0]
arr[0] = tem
print(arr)


#25
arr = [1,2,3,4,5,6]
i = 0
j=len(arr)-1
while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1
print(arr)


#26
arr = [1,22,3,42,5,6]
max = float('-inf')
min = float('inf')
for ele in arr:
    if max<ele:
        max = ele
    if min>ele:
        min = ele
print(f"max: {max}\nmin: {min}")

#28
arr = [23,33,5,1,55,85]
search = 34
if search in arr:
    print("element found")
else:
    print("element not found")


#30
arr1 = [1,2,5,6,7,12]
arr2 = [23,22,12,9,3]
newArr = []
p1 = 0
p2 = len(arr2)-1

while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]>arr2[p2]:
        newArr.append(arr2[p2])
        p2-=1
    else:
        newArr.append(arr1[p1])
        p1+=1

print(p1, p2)
while(p1<len(arr1)):
    newArr.append(arr1[p1])
    p1+=1

while(p2!=-1):
    newArr.append(arr2[p2])
    p2-=1
print(newArr)




#31
arr1 = [10,9,8,7,6,5,4,3]
arr2 = [54,45,16,10,9,5]
newArr = []

p1 = 0
p2 = 0
while(p1!=len(arr1) and p2!=len(arr2)):
    if arr1[p1]>arr2[p2]:
        newArr.append(arr1[p1])
        p1+=1
    else:
        newArr.append(arr2[p2])
        p2+=1
while(p1!=len(arr1)):
    newArr.append(arr1[p1])
    p1+=1
while(p2!=len(arr2)):
    newArr.append(arr2[p2])
    p2+=1
print(newArr)


#32
a = [3,2,1,7,6,3]
b = [9,3,5,6,2,8,10]
result=[]
for element in a:
    if element%2==0:
        result.append(element)
for element in b:
    if element%2==0:
        result.append(element)
for i in range(len(b)-1, -1,-1):
    if b[i]%2!=0:
        result.append(b[i])
for i in range(len(a)-1, -1,-1):
    if a[i]%2!=0:
        result.append(a[i])
print(result)



#33 and 29
arr = [2, 3, 4, 6, 5, 4, 4, 1, 2, 1]
search = int(input("enter searching element: "))
low = 0
arr.sort()
flag = 0
high = len(arr)-1
while low<high:
    mid = int((high+low)/2)
    if arr[mid]==search:
        flag = 1
        break
    if arr[mid]>search:
        high = mid-1
    else:
        low = mid+1

if flag==1:
    print(f"element found")
else:
    print(f"element not found")


#34
arr = [2, 3, 4, 6, 5, 4, 4, 1, 2, 1]
search = int(input("enter searching element: "))
for i in range(0, len(arr)):
    if arr[i]==search:
        print(f"element found at idx: {i}")
        break


#35
arr = [2, 3, 4, 6, 5, 4, 4, 1, 2, 1]

for i in range(0, len(arr)):
    min = i 
    for j in range(i+1, len(arr)):
        if arr[min]>arr[j]:
            min = j
        tem = arr[min]
        arr[min] = arr[i]
        arr[i]  = tem
print(arr)


#36
demolist = [45,34,12,43,54,23,44]
for i in range(0, len(demolist)):
    for j in range(i+1, len(demolist)):
        if (demolist[i]>demolist[j]):
            temp = demolist[i]
            demolist[i] = demolist[j]
            demolist[j] = temp

print(demolist)


#37
demolist = [45,34,12,43,54,23,44]
for i in range(1,len(demolist)):
    

'''
