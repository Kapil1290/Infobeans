n = 5
'''
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for j in range(1, 2*i+1):
        if j==1 or j==2*i:
            print("*", end="")
        else:
            if i==3:
                print("*", end="")
            else:
                print(" ", end="")
    print()

n = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==1 and i>=j:
            print("*", end="")
        elif j==n and i<=j:
            print("*", end="")
        elif i==3 :
            print("*", end="")
        elif i==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''
n = 6

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==1 and i>=j:
            print("*", end="")
        elif i==n and j<=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif i==n and j<=i:
            print("*", end="")
        elif j==n//2-1:
            print("*", end="")
        elif j==n and i<=j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif i==n and j<=i:
            print("*", end="")
        elif i==3 :
            print("*", end="")
        elif j==1 and j<=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif i==3 :
            print("*", end="")
        elif j==1 and j<=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
n=6
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==1 and i>=j:
            print("*", end="")
        elif i==n and j<=i:
            print("*", end="")
        elif i==4 and j>=4:
            print("*", end="")
        elif j==n and i>=4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 and i>=j:
            print("*", end="")
        elif j==n and j>=i:
            print("*",end="")
        elif i==3:
            print("*",end="")
        else:
            print(" ", end="")
    print()
print()
n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==3 :
            print("*", end='')
        elif i==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==3 :
            print("*", end='')
        elif i==n and j<4:
            print("*", end="")
        elif i==n-1 and j<2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=7
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 and i>=j:
            print("*", end="")
        elif i+j==n:
            print("*", end="")
        elif i-j==2:
            print("*", end='')
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 and i>=j:
            print("*", end="")
        elif j==n and j>=i:
            print("*",end="")
        elif i==j and i<=3:
            print("*", end="")
        elif i==2 and j==4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 and i>=j:
            print("*", end="")
        elif j==n and j>=i:
            print("*",end="")
        elif i==j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 and i>=j:
            print("*", end="")
        elif j==n and j>=i:
            print("*",end="")
        elif i==1 and i<=j:
            print("*", end="")
        elif i==n and j<=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==1 and i>=j:
            print("*", end="")
        elif j==n and i<=3:
            print("*", end="")
        elif i==3 :
            print("*", end="")
        elif i==n and j==1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 and i>=j:
            print("*", end="")
        elif j==n and j>=i:
            print("*",end="")
        elif i==1 and i<=j:
            print("*", end="")
        elif i==n and j<=i:
            print("*", end="")
        elif i==n-1 and j==n-2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print('     *')


n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==1 and i>=j:
            print("*", end="")
        elif j==n and i<=3:
            print("*", end="")
        elif i==3 :
            print("*", end="")
        elif i==n and j==1:
            print("*", end="")
        elif i==n-1 and j==3:
            print("*", end="")
        elif i==n and j==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==1 and i!=n-1:
            print("*", end="")
        elif j==n and i!=2:
            print("*", end="")
        elif i==3 :
            print("*", end="")
        elif i==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()


n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j>=i:
            print("*", end="")
        elif j==3 :
            print("*", end='')
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 and i>=j:
            print("*", end="")
        elif j==n and j>=i:
            print("*",end="")
        elif i==n and j<=i:
            print("*", end="")
        
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n*2):
        if i==j:
            print("*", end="")
        elif i+j==(n*2):
            print("*",end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(n, 0, -1):
    for j in range(1, n+1):
        if j==1 and i>=j:
            print("*", end="")
        elif j==n and j>=i:
            print("*",end="")
        elif i==j and i<=3:
            print("*", end="")
        elif i==2 and j==4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        
        if i==j:
            print("*", end="")
        elif i+j==n+1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i+j==n+1:
            print("*", end="")
        elif j==i and i<=3:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and i<=j:
            print("*", end="")
        elif i+j==n+1:
            print("*", end="")
        elif i==n and j<=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()