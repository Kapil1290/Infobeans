# n = int(input("enter a number:- "))
ans = 0

for _ in range(1,n+1):
    if(n==0):
        ans//=10
        break  
    rem = n%10
    ans = (ans+rem)*10
    n = int(n/10)
print((ans))


n = int(input("enter a number for checking palindrome:-"))
value=n
for _ in range(1,n+1):
    if(n==0):
        ans//=10
        break  
    rem = n%10
    ans = (ans+rem)*10
    n = int(n/10)
if ans==value:
    print("number is palidrome")
else :
    print("number is not palindrome")


# number = int(input("enter number: - "))
# power  = int(input("enter power:- "))
# ans=1
# for i in range(1,power+1):
#     ans *= number
# print(ans)


n = int(input("enter number:- "))
value=0
safe = n
for _ in range(1,n+1):
    if(n==0):
        ans//=10
        break  
    rem = n%10
    value += rem**3
    n = int(n/10)
if(safe==value):
    print(f"{safe} is armstrong number")
else:
    print(f"{safe} is not a armstrong number")


# n = int(input("enter a number:- "))
# value=0
# for _ in range(1,n+1):
#     if(n==0):
#         ans//=10
#         break  
#     rem = n%10
#     value += rem
#     n = int(n/10)
# print(value)



# n = int(input("enter a number:- "))
# value=0
# for _ in range(1,n+1):
#     if(n==0):
#         ans//=10
#         break  
#     rem = n%10
#     value+=1
#     n = int(n/10)
# print(value)



n = int(input("enter number for checking the perfect number:- "))
value=0
for i in range(1,n):
    if(n%i==0):
        value=value+i
if(n==value):
    print("perfect number")
else:
    print("not perfect number")


n = int(input("enter a number:-"))
value=n
total_count=0
even_count=0
for _ in range(1,n+1):
    if(n==0):
        ans//=10
        break  
    rem = n%10
    if(rem%2==0):
         even_count+=1
    total_count+=1
    n = int(n/10)

print(f"Even count is:- {even_count} \nOdd count is:- {total_count-even_count}")


