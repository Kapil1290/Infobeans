# Transpose of the matrix 
'''
list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [3,2,1,5]
]
print(list)

for row in range(len(list)):
    for col in range(row, len(list[row])):
        if row!=col:
            tem = list[row][col]
            list[row][col] = list[col][row]
            list[col][row] = tem 

print(list)

# Upper trangular
list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [3,2,1,5]
]

for i in range(len(list)):
    for j in range(len(list[i])):
        if i<=j:
            print(list[i][j], end=" ")


# Lower trangular
list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [3,2,1,5]
]

for i in range(len(list)):
    for j in range(len(list[i])):
        if i>=j:
            print(list[i][j], end=" ")


# Left Diagonal
list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [3,2,1,5]
]

for i in range(len(list)):
    for j in range(len(list[i])):
        if i==j:
            print(list[i][j], end=" ")


#Right Diagonal
list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

for i in range(len(list)):
    for j in range(len(list[i])):
        if (i+j)==(len(list)-1):
            print(list[i][j], end=" ")
'''

# Multiply Matrix
a = [
    [1,2,3],
    [3,4,5],
    [9,0,8]
]

b = [
    [1,2,3],
    [3,4,5],
    [9,0,8]
]
c = [
    [0]*3,
    [0]*3,
    [0]*3
]

for i in range(len(a)):
    for j in range(len(a[i])):
        val = 0
        for k in range(len(a[i])):
            val += (a[i][k]*b[k][j])
        c[i][j]=val
        print(val)
    print("\n")

print(c)

