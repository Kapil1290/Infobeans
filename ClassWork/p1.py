n = int(input("enter number n:- "))
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
for _ in range(n):
    print(a,end="  ")
    c=a*b 
    a=b 
    b = c 

for i in range(65, 91):
    print(chr(i+32), end=" ")

sum = 0
for i in range(1,n+1):
    sum += 1/i
print(int(sum))