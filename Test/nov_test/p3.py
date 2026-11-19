str1 = "babad"

for i in range(0, len(str1)):
    for j in range(i, len(str1)):
        tem = str1[i:j]
        if tem == str1[0:-2]:
            print(tem)