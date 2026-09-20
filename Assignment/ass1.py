'''import string
# 1
i=1
while(i<=1000):
  print("Hello from Kapil!!!!!")
  i=i+1


# 2
n = int(input("enter n"))
i=1
while(i<=n):
  print(i)
  i=i+1

# 3
n = int(input("enter n"))
i=1
sum = 0
while(i<=n):
  sum += i
  i=i+1
print("sum is", sum)

# 4
n = int(input("enter n"))
i=1
while(i<=10):
  print(i*n)
  i=i+1

# 5
n = int(input("enter n"))
sum = 1
while(0==n):
  sum *= n
  n=n-1

print("factorial of",n,"is ", sum )


# 6
n = int(input("enter num"))
i=1
print("factors are:- \n")
while(i<=n):
  if(n%i==0):
    print(i)
  i=i+1
'''

'''
# 7
n = int(input("enter num n"))
i=2
flag=0
while(i<=n//2):
  if(n%i==0):
    flag=1
    break
  i=i+1

# if(flag==0 or n<2):
#   print(f"{n} is prime")
# else:
#   print(f"{n} is not prime")

if i>n//2 and n>1:
    print("prime")
else:
    print("not a prime")
    

# 8
n = int(input("enter num n"))
i=0
a,b = 0,1
print(a,"\n",b)
while(i<n):
  print(a+b)
  tem = a
  a = b  
  b = tem+b
  i=i+1
  

# 9
n = int(input("enter num n"))
i=2

while(i<=1000000000):
  if(i%2==0):
   print(i)
  if(i==n):
   break
  i=i+1


# 10
n = int(input("enter num n"))
i=2

while(i<=1000000000):
  if(i%2==0):
   print(i)
  if(i==n):
   break
  i=i+1

# 11
n = int(input("enter num n"))
i=2

while(i<=1000000000):
  if(i%2!=0):
   print(i)
  if(i==n):
   break
  i=i+1

# 12
n = int(input("enter num n"))
i=2

while(i<=1000000000):
  if(i%2!=0):
   print(i)
  if(i==n):
   break
  i=i+1

# 13
n = int(input("enter num n"))
while(n!=0):
  print(n)
  n=n-1

# 14
alphabet = "A"
lowercase = string.ascii_lowercase
print(lowercase)

# 15
uppercase = string.ascii_uppercase
print(uppercase)

# 16
n = int(input("enter num n"))
i = -6
x=0
while(i<=1000000):
  print(i)
  x=x+1
  if(n==x):
    break
  i=i+3
  
# 17
n = int(input("enter num n"))
i=1
x=0
while(x<=n):
  print(i)
  x=x+1
  i=i+x


# 18
n = int(input("enter num n"))
i=1
j=2
print(i,"\n",j)
while(n!=0):
  print(i*j)
  tem=i
  i=j
  j = tem*j
  n=n-1

# 19
term = int(input("enter num n:- "))
number = 1
value = 0
while term > 0:
  value = value+1/num
  
# 20
n = int(input("enter num n"))
i = 0 
while(n!=0):
  print(i)
  i=i+7
  n=n-1

# 21
n = int(input("enter num n"))
i = 3
x=1
print(x)
while(n!=0):
  if(i%2!=0):
    print(x+i)
    x=x+i
    n=n-1
  i=i+1

# 22
n = int(input("enter number n:- "))
i = 1
for _ in range(1, n):
  print(i*i*i)
  i+=1


# 23
n = int(input("enter number n:- "))
i = 1
for _ in range(1, n):
  print(i*i)
  i+=2


# 24
n = int(input("enter number n:- "))
i = 0
for _ in range(1, n):
  print(i*i)
  i+=2


n = int(input("enter number n:- "))
i = 1
for _ in range(1, n):
  print(i*i*i)
  i+=2
 

n = int(input("enter number n:- "))
i = 0
for _ in range(1, n):
  print(i*i*i)
  i+=2



n = int(input("enter number n:- "))
for i in range(1, n+1):
  if i%2==0 :
    print("*", end=" ")
  else :
    print("#", end=" ")



n = int(input("enter number n:- "))
for i in range(1, n+1):
  if i%5==0 :
    print("Hello",end=" ")
  else :
    print(i, end=" ")


n=int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(1, i+1):
    print("1", end=" ")
  print(end="  ")
  

n=int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(1, i+1):
    print("9", end=" ")
  print(end="  ")
  

n = int(input("enter number n:- "))
x = 1
capital=65
small = 97
for _ in range(1, n+1):
  if(x%2==0):
    print(chr(small), end=" ")
    capital+=1
    small+=1
  else:
    print(chr(capital), end=" ")
    small+=1
    capital+=1
  x+=1


alphabet = 90
for i in range(alphabet, 64, -1):
  print(chr(i), end=" ")



n = int(input("enter number n:- "))
ans = 1
xtra=2
while(n!=1):
  if(n%xtra==0):
    ans *= xtra
    n //= xtra
  else:
    xtra+=1
print(ans)

# hcf que rem

n = int(input("enter binary number :- "))
temVar=0
ans = 0
while(n!=0):
  remender = n%10
  if(remender==1):
    ans += 2**temVar
  temVar+=1
  n//=10

print(ans)
'''

n = int(input("enter number greater than 9 :- "))

