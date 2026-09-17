import string
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

# 7
n = int(input("enter num n"))
i=2
flag=0
while(i<n):
  if(n%i==0):
    flag=1
    break
  i=i+1

if(flag==0):
  print(f"{n} is prime")
else:
  print(f"{n} is not prime")

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
  value = value+
  
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

