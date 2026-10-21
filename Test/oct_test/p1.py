val = int(input("Enter number for checking Harshed Number: "))
backup=val
sum=0
while val!=0:
    rem = val%10
    sum += rem
    val//=10
if backup%sum==0:
    print("harshed number")
else:
    print("Not harshed num")