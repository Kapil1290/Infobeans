

units = int(input("enter unit that you consumed: "))
total = 0
if units<=100:
    total+=units*5:
elif units<=200:
    total +=500
    units-=100
    total 

    

print(f"total is : {total}")

'''

a = int(input("enter number a: "))
b = int(input("enter number b: "))
n = input("enter number: -")

match(n):
 case '+': print(a+b)
 case "-": print(a-b)
 case "/": print(a/b)
 case "%": print(a%b)
 case _: print("invalid Operator")

 #-------------------


n = int(input('enter number : '))
safe = n
count=0
sum =0
ans = 0
check = []
while n!=0:
    rem = n%10
    check.append(rem)
    ans = (ans*10)+rem
    count+=1
    sum += rem
    n//=10

if ans==safe:
    print("it is palindrome")
else:
    print("not palindrome")
print(f"count is {count}")
print(f"sum is {sum}")

check.sort()
print(f"largest value is : {check[len(check)-1]}")
print(f"largest value is : {check[0]}")

 #-------------------



start = int(input("enter number 1: "))
end= int(input("enter number 2 : "))
flag = 0
count=0
for j in range(start+1, end):
    flag=0
    for i in range(2,j):
        if j%i==0:
            flag=1
            break
    if flag==0:
        print(j)
        count+=1

print(f"Total prime numbers are : {count}")  



programm = 0
math = 0
english =0

while 1:
    print("enter 1 for enter marks")
    print("enter 2 for finding average")
    print("enter 3 for largest")
    print("enter 4 for minimum")
    print("enter 5 for display result in percent")
    print("enter 6 for exit")
    choice = int(input("enter choice: "))
    match choice:
      case 1:
               programm = int(input("enter programing number : "))
               math = int(input("enter math number : "))
               english = int(input("enter english number : "))
               print(f"total marks are {programm+math+english} \n\n")
      case 2: 
               print(f"Average of the number is {float((programm+math+english)/3)}")
      case 3: 
               if programm!=0:
                if programm>math:
                  if(programm>english):
                      print("Programing marks are greater___")
                  else:
                      print("English marks are greater___")
                else:
                  if math>english:
                    print("Math marks are greater")
                  else:
                    print("English marks are greater")
               else:
                print("pls enter marks first\n\n\n")
      case 4:
              if programm!=0:
                if programm<math:
                  if(programm<english):
                      print("Programing marks are lowest")
                  else:
                      print("English marks are lowest")
                else:
                  if math<english:
                    print("Math marks are lowest")
                  else:
                    print("English marks are greater")
              else:
                print("pls enter marks first")
              print("\n\n\n")
      case 5:
             if programm!=0 and math!=0:
                print(f"Total Percentage: {(programm+math+english)/3}")
             else:
                print("Please enter marks first: ")
             print("\n\n\n")
      case 6:
             break
    

 '''
   
