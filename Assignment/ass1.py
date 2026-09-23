import math
'''
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

# first and last digit


value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))
for i in range(value1, value2+1):
  for j in range(1, 11):
    print(i*j, end=" ")
  print()


# not correct
value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))
ans = 0
print("number palidrome:- ")
for n in range(value1, value2+1):
  n_reference=n
  while n!=0:
     
    rem = n%10
    ans = (ans+rem)*10
    n = int(n/10)
    # print(ans, end=" ")
  # print(ans, end="  ")
  ans=ans//10
  # print(ans)
  
  if ans==n_reference:
    print(ans, end=" ")
  ans=0

value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))
ans=0
for n in range(value1, value2+1):
  while n!=0:
    if(n==0):
        ans//=10
        break  
    rem = n%10
    ans = (ans+rem)*10
    n = int(n/10)
  ans //=10
  print((ans))
  ans = 0


value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))

value=0

for n in range(value1, value2+1):
  safe = n
  while n!=0 :
    if(n==0):
      ans//=10
      break  
    rem = n%10
    value += rem**3
    n = int(n/10)
  if(safe==value):
    print(f"{safe} is armstrong number")
  value=0


value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))
value=0
for n in range(value1, value2+1):
  for i in range(1,n):
    if(n%i==0):
      value=value+i
  if(n==value):
    print("perfect number ",n)
  value=0


value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))
for n in range(value1, value2+1):
  if n%2==0:
    print(n, end=" ")

value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))
for n in range(value1, value2+1):
  if n%2!=0:
    print(n, end=" ")


value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))
ans = 1
for n in range(value1, value2+1):
  while n!=0:
    rem = n%10
    if rem!=0:
      for i in range(rem, 1, -1):
        ans *= i
    n//=10
  print(ans, end=" ")
  ans = 1


n = int(input("enter number n:- "))
for i in range(1,n+1):
  print(i*i," ",i*i*i, " ", int(math.sqrt(i)))


value1 = int(input("enter number 1 :- "))
value2 = int(input("enter number 2:- "))
for n in range(value1, value2+1):
  if(n%4==0 and n%100!=0) or (n%400==0):
    print(n, end=" ")


# 1

n = int(input("enter number:- "))
for i in range(1, n):
  print("*", end="")
#2
n = int(input("enter number:- "))
for i in range(1, n):
  print("*")

#3
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(i-1, 0, -1):
    print(" ", end="")
  print("*")

#4
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(1, n+1):
    print("*", end="")
  print()

#5
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(1, n+1):
    print(j, end="")
  print()

#6
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(1, n+1):
    print(i, end="")
  print()

#7
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(i, 0, -1):
    if i%2==0:
      print("0", end="")
    else:
      print("1", end="")
  print()

#8
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(i, 0, -1):
    print("*", end="")
  print()

#9
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(1, i+1):
    print(j, end="")
  print()
#18
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(1, i+1):
    if j%2==0:
      print("0", end="")
    else:
      print("1", end="")
  print()
#13
n = int(input("enter number:- "))
for i in range(1, n+1):
  for j in range(1, i+1):
    if j%2==0:
      print("1", end="")
    else:
      print("0", end="")
  print()

#15
n = int(input("enter nmber :- "))
alphabet=65
for j in range(1, n+1):
  for i in range(1, j+1):
    print(chr(alphabet), end="")
  print()
  alphabet+=1

#30
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(i, 0, -1):
    print("*", end="")
  print()

#31
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(1, i+1):
    print(j, end="")
  print()

#32
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(1, i+1):
    print(i, end="")
  print()
  
# not done
n = int(input("enter number n:- "))
increment=1
for i in range(1, n+1):
  for j in range(1, increment+1):
    print("*", end="")
  print()
  increment+=1

# 41
n = int(input("enter number n:- "))
alphabet=65
for i in range(1, n+1):
  for j in range(1, 2*i-1+1, 1):
    print(chr(alphabet), end=" ")
    alphabet+=1
  print()

#49
n = int(input("enter number n:- "))
for i in range(1, n+1):
  for k in range(n, i, -1):
    print(" ", end="")
  for j in range(1, i+1):
    if(j%2!=0):
      print("1",end="")
    else:
      print("0",end="")
  print()

#51
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for k in range(n-i, 0,-1):
    print(" ", end="")
  for j in range(1, i+1):
    print(i, end="")
  print()

#89
n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(1, n-i+1):
    print(" ", end="")
  for k in range(1, 2*i-2):
    if(k%2==0):
      print("0", end="")
    else:
      print("1", end="")
  print()

#61
n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(1, n-i+1):
    print(" ", end="")
  for k in range(1, 2*i-2):
    print("*", end="")
  print()

#40
n = int(input("enter number n:- "))
for i in range(1, n+1):
  
  for k in range(1, 2*i-2):
    print("*", end="")
  print()

#28
n = int(input("enter number n:- "))
for i in range(1, n+1):
  
  for k in range(1, 2*i-2):
    print(k, end="")
  print()

#43
n = int(input("enter number n:- "))
for i in range(1, n+1):
  
  for k in range(1, i):
    print(k, end="")
  print()

#45
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(1, i):
    print(" ", end="")
  for k in range(1, n-i+2):
    print(i, end="")
  print()

#44
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(1, i):
    print(" ", end="")
  for k in range(1, n-i+2):
    print(k, end="")
  print()


#42
n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(5, i-1, -1):
    print(j, end="")
  print()

#58
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(1, i):
    print(" ", end="")
  for k in range(1, n-i+2):
    print(k, end=" ")
  print()

#57
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(1, i):
    print(" ", end="")
  for k in range(1, n-i+2):
    print("*", end=" ")
  print()

#39
n = int(input("enter number n:- "))
for i in range(1, n+1):
  if(i%2!=0):
    for j in range(1, n-i+2):
      print(j, end="")
  else:
    for j in range(n-i+1, 0, -1):
      print(j, end="")
  print()

#16
n = int(input("enter number n:- "))
alphabet = 97
for i in range(1, n+1):
  for j in range(1, i+1):
    print(chr(alphabet), end="")
    alphabet+=1
  print()
  
#17
n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(1, i+1):
    if(i%2==0):
      print("#", end="")
    else:
      print("*", end="")
  print()

#19
n = int(input("enter number n:- "))
for i in range(1, n+1):
  print("*", end="")

  for j in range(1, i-2+1):
    if(i!=n):
      print("-", end="")
  if(i>1):
    print("*", end="")
  if(i==n):
    for k in range(1, n-1):
      print("*", end="")
  print()

#20
n = int(input("enter number n:- "))
for i in range(1, n+1):
  if i!=n:
    print("1", end="")
    for j in range(1, i-2+1):
      if(i!=n):
        print("-", end="")
    if(i>1):
      print(i, end="")
  if(i==n):
    for k in range(1, n+1):
      print(k, end="")
  print()

#21
n = int(input("enter number n:- "))
for i in range(1, n+1):
  print(i, end="")

  for j in range(1, i-2+1):
    if(i!=n):
      print(" ", end="")
  if(i>1):
    print(i, end="")
  if(i==n):
    for k in range(1, n-1):
      print(i, end="")
  print()

#22
n = int(input("enter number n:- "))
for i in range(1, n+1):
  alphabet=65
  for j in range(1, i+1):
  
    if j==1 or j==i or i==n:
      print(chr(alphabet), end="")
    else:
      if j!=n:
        print(" ", end="")
      
    alphabet+=1
  print()
#23
n = int(input("enter number n:- "))
alphabet=97
for i in range(1, n+1):
  
  for j in range(1, i+1):
  
    if j==1 or j==i or i==n:
      print(chr(alphabet), end="")
    else:
      if j!=n:
        print(" ", end="")
    alphabet+=1
  print()
#24
n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(1, i+1):
  
    if j==1 or j==i or i==n:
      print("* ", end="")
    else:
      if j!=n:
        print("@ ", end="")
  print()

#25
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(5, i-1, -1):
    print(j, end="")
  print()

#26
n = int(input("enter number n:- "))
for i in range(1,n+1):
  for j in range(1, i+1):
    if(j%2==0):
      print("#",end="")
    else:
      print("*", end="")
  print()

#27
n = int(input("enter number n:-- "))
for i in range(1, n+1):
  for j in range(1, i+1):
    if((j==1 or j==i) and i!=n):
      if(j%2==0):
        print("0", end="")
      else:
        print("1", end="")
    else:
      if(i!=n):
        print(" ", end="")
      else:
        if(j%2==0):
          print("0", end="")
        else:
          print("1", end="")   
  print()

#28
n = int(input("enter number n:- "))
for i in range(1, n+1):
  alphabet=65
  for j in range(1, n-i+1):
    print(chr(alphabet), end="")
    alphabet+=1
  print()

#33
n = int(input("enter number n:- "))
alphabet=69
for i in range(1, n+1):
  
  for j in range(1, n-i+2):
    print(chr(alphabet), end="")
    
  alphabet-=1
  print()

#34
n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(n, 0, -1):
    if (j==n or j==i) and i!=1 :
      print("*", end="")
    else:
      if(i==1):
        print("*", end="")
      else:
        print(" ", end="")
  print()

#35
n = int(input("enter number n:- "))
for i in range(1, n+1):
  alphabet=65
  for j in range(1, n-i+2):
    if (j==1 or j==n-i+1) and i != 1:
      print(chr(alphabet), end="")
      alphabet+=1
    else:
      if(i==1):
        print(chr(alphabet), end="")
        alphabet+=1
      else:
        print(" ", end="")
        alphabet+=1
  print()

#36
n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(n, i-1, -1):
    if(i%2==0):
      print("#", end="")
    else:
      print("*", end="")
  print()

#37
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(1, i+1):
    if j==1 or j==i:
      print(i, end="")
    else:
      if(i==n):
        print(i, end="")
      else:
        print(" ", end="")
  print()

#38
n = int(input("enter number n:- "))

for i in range(1, n+1):
  alphabet=65
  for j in range(1, n-i+1):
    print(" ", end="")
  for j in range(1, i+1):
    print(chr(alphabet), end="")
    alphabet+=1
  print()
#46
n = int(input("enter number n:- "))
for i in range(1, n+1):
  alphabet=65
  for j in range(1, n-i+1):
    print(" ", end="")
  for j in range(1, i+1):
    if j==1 or j==i:
      print("1", end="")
    else:
      if(i==n):
        print('1', end="")
      else:
        print("*", end="")
  print()

#47
n = int(input("enter number n:- "))
for i in range(1, n+1):
  alphabet=65
  for j in range(1, n-i+1):
    print(" ", end="")
  for j in range(1, i+1):
    if j==1 or j==i:
      print(chr(alphabet), end="")
      alphabet+=1
    else:
      if(i==n):
        print(chr(alphabet), end="")
        alphabet+=1
      else:
        print("_", end="")
  print()
#  48
n = int(input("enter number n:- "))
for i in range(n, 0, -1):
  for j in range(1, i):
    print(" ", end="")
  for k in range(1, n-i+2):
    print("*", end=" ")
  print()


#62
n = 5
for i in range(1, n+1):
  for j in range(1, n-i+1):
    print(" ", end="")
  for j in range(1, 2*i-2):
    print(j, end="")
  print()

#91
n = 5
for i in range(1, n+1):
  for j in range(1, n-i+2):
    print(" ", end="")
  for j in range(1, 2*i-2):
    print("*", end="")
  print()

for i in range(n-1, 0, -1):
  for j in range(n-i+1, 0, -1):
    print(" ", end="")
  for j in range(2, 2*i-1):
    print("*", end="")
  print()

#69
n = 5
for i in range(n, 0, -1):
  for j in range(n-i+1, 0, -1):
    print(" ", end="")
  for j in range(2, 2*i-1):
    print("*", end="")
  print()  

#31
n=5
for i in range(n, 0, -1):
  for j in range(n-i, 0, -1):
    print(" ", end="")
  for j in range(1, i+1):
    print(j, end="")
  print()


n = 5
for i in range(n, 0, -1):
  for j in range(n-i, 0, -1):
    print(" ", end="")
  for j in range(1, i+1):
    if j==1 or j==i:
      print(j, end="")
    else:
      if(i==n):
        print(j, end="")
      else:
        print("_", end="")
  print()

n = 5
for i in range(1, n+1):
  for j in range(n, n-i+1, -1):
    print(" ", end="")
  for j in range(1, n-i+2):
    print(i, end="")
  print()


n = 5
for i in range(1, n+1):
  for j in range(1, n-i+1):
    print(" ", end="")
  for j in range(1, i+1):
    print("* ", end="")
  print()


n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(1, n-i+1):
    print(" ", end="")
  for k in range(1, 2*i):
    if k==1 or k==2*i-1:
      print("*", end="")
    else:
      if(i==n):
        print("*", end="")
      else:
        print("_", end="")
  print()


n = 5
for i in range(1, n+1):
  for j in range(1, n-i+1):
    print(" ", end="")
  for j in range(1, 2*i):
    print(j, end="")
  print()

n = 5
for i in range(1, n+1):
  alphabet=65
  for j in range(1, n-i+1):
    print(" ", end="")
  for j in range(1, 2*i):
    print(chr(alphabet), end="")
    alphabet+=1
  print()

n = int(input("enter number n:- "))
for i in range(1, n+1):
  for j in range(1, n-i+1):
    print(" ", end="")
  for k in range(1, 2*i):
    if k==1 or k==2*i-1:
      print("X", end="")
    else:
      if(i==n):
        print("X", end="")
      else:
        print("_", end="")
  print()

#90
n = 7
for i in range(1, n+1):
  for j in range(1, n+1):
    if i==j or i+j==8:
      print("*", end="")
    else:
      print(" ", end="")
  print()

#88
n = 9
for i in range(1, n+1):
  for j in range(1, n+1):
    if j>=i and j==5:
      print(i, end="")
    elif i>j and i==5:
      print(j, end="")
    elif i>j and j==5:
      print(10-i, end="")
    elif j>i and i==5:
      print(10-j, end="")
    else:
      print(" ", end="")
  print()

n = 10
for i in range(1, n+1):
  for j in range(n//2, i-1, -1):
    print("*", end="")
  for j in range(1, i-1):
    print(" ", end="")
  for j in range(n//2, i-1, -1):
    print("*", end="")
  print()

n=10
for i in range(n, 0, -1):
  for j in range(n//2, i-1, -1):
    print("*", end="")
  for j in range(i-1, 0, -1):
    print(" ", end="")
  for j in range(n//2, i-1, -1):
    print("*", end="")
  print()
'''
#87
n = 10
for i in range(1, n+1):
  for j in range(n//2+1, i, -1):
    print("*", end="")
  if i<6:
    for j in range(1, i):
      print(" ", end="")
  for j in range(n//2+1, i, -1):
    print("*", end="")
  if(i!=6):
    print()
  if i>(n//2):
    for j in range(1, i-(n//2)+1):
      print("*", end="")
    for j in range(1, n-i+1):
      print(" ", end="")
    for j in range(1, i-(n//2)+1):
      print("*", end="")
'''
n = 5
for i in range(1, n+1):
  for j in range(1, n-i+2):
    print(" ", end="")
  for j in range(1, 2*i):
    if j==1 or j==2*i-1 :
      print("*", end="")
    else:
      print("_", end="")
  print()

for i in range(n-1, 0, -1):
  for j in range(n-i+1, 0, -1):
    print(" ", end="")
  for j in range(2, 2*i+1):
    if j==2 or j==2*i:
      if j%2==0:
        print("*", end="")
      else:
        print("_", end="")
    else:
      print("_", end="")
  print()

n = 5
for i in range(1, n+1):
  for j in range(1, n-i+2):
    print(" ", end="")
  for j in range(1, 2*i):
    if j%2==1:
      print("*", end="")
    else:
      if j==1 or j==2*i-1 :
        print("*", end="")
      else:
        print("_", end="")
  print()

for i in range(n-1, 0, -1):
  for j in range(n-i+1, 0, -1):
    print(" ", end="")
  for j in range(2, 2*i+1):
    if j%2==0:
      print("*", end="")
    else:
      if j==2 or j==2*i:
        print("*", end="")
      else:
        print("_", end="")
  print()

n = 5
for i in range(1, n+1):
  for j in range(1, n-i+2):
    print(" ", end="")
  for j in range(1, 2*i):
    if j==1 or j==2*i-1:
      print("1", end="")
    else:
      if i==n:
        print("1", end="")
      else:
        print("*", end="")
  print()

n=5
alphabet=65
for i in range(1, n+1):
  for j in range(1, n-i+2):
    print(" ", end="")
  for j in range(1, 2*i):
    if j==1 or j==2*i-1:
      print(chr(alphabet), end="")
    else:
      if i==n:
        print(chr(alphabet), end="")
      else:
        print("*", end="")
  print()
  alphabet+=1
  
#69
n = 5
for i in range(1, n+1):
  for j in range(1, n-i+2):
    print(" ", end="")
  for j in range(1, 2*i):
    if(j==2*i or i==j):
      print("#", end="")
    else:
      print("*", end="")
  print()

#70
n = 5 
for i in range(n, 0, -1):
  for j in range(1,n-i+1):
    print(" ", end="")
  for j in range(1, i+1):
    print("* ", end="")
  print()


n = 5
for i in range(1, n+1):
  for j in range(1, i+1):
    print(" ", end="")
  for j in range(1, 2*(n-i)+2):
    print(j, end="")
  print()

n = 5
for i in range(1, n+1):
  alphabet=65
  for j in range(1, i+1):
    print(" ", end='')
  for j in range(1, n-i+2):
    print(chr(alphabet),"", end="")
    alphabet+=1
  print()


n = 5
for i in range(1, n+1):
  for j in range(1, i+1):
    print(" ", end='')
  for j in range(1, 2*(n-i)+2):
    if(j==1 or j==2*(n-i)+1):
      print(j, end="")
    else:
      if(i==1):
        print(j, end="")
      else:
        print(" ", end="")
  print()

n = 5
for i in range(1, n+1):
  for j in range(1, i+1):
    print(" ", end='')
  for j in range(1, 2*(n-i)+2):
    if(j==1 or j==2*(n-i)+1):
      print(j, end="")
    else:
      if(i==1):
        print(j, end="")
      else:
        print("+", end="")
  print()  

n = 5
for i in range(1, n+1):
  for j in range(1, i+1):
    print("x", end="")
  print()
for i in range(n-1, 0, -1):
  for j in range(1, i+1):
    print("x", end="")
  print()

n = 5
for i in range(1, n+1):
  for j in range(1, i+1):
    print(j, end="")
  print()
for i in range(n-1, 0, -1):
  for j in range(1, i+1):
    print(j, end="")
  print()

n=5
for i in range(n-1, 0, -1):
  for j in range(1, i+1):
    print(" ", end="")
  for j in range(1, n-i+1):
    print(j, end="")
  print()
for i in range(2, n-i+1):
  for j in range(1, i+1):
    print(" ", end="")
  for j in range(1, n-i+1):
    print(j, end="")
  print()

n = 5
for i in range(1, n+1):
  for j in range(1, i+1):
    if j==1 or j==i:
      print(j, end='')
    else:
      print(" ", end="")
  print()
for i in range(n-1, 0, -1):
  for j in range(1, i+1):
    if j==1 or j==i:
      print(j, end='')
    else:
      print(" ", end="")
  print()


n = 5
for i in range(1, n+1):
  for j in range(n-i, 0, -1):
    print(" ", end="")
  for j in range(i, 0, -1):
    print(j, end="")
  for j in range(2,i+1):
    print(j, end="")
  print()

n = 7
for i in range(1, n+1):
  for j in range(1, n+1):
    if (i+j)==(n+1):
      print("*", end="")
    elif i==n:
      print("*", end="")
    elif i==j:
      print("*", end="")
    elif (i==1 and j>=i):
      print("*", end="")
    elif i==n and i>=n:
      print("*", end="")
    elif j==1 and i>=j:
      print("*", end="")
    elif j==n and j>=i:
      print("*", end="")
    else:
      print(" ", end="")
  print()

n = 9
for i in range(1, n+1):
  for j in range(1, n+1):
    if j>=i and j==5:
      print(i, end="")
    elif i>j and i==5:
      print(j, end="")
    elif i>j and j==5:
      print(10-i, end="")
    elif j>i and i==5:
      print(10-j, end="")
    else:
      print(" ", end="")
  print()
'''

# n = 5
# for i in range(1, n+1):
