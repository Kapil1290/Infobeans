
l1 = [10,20,30,40,50]
l2 = [30, 40, 60, 70]
unique=[]
common = []


for i in range(0, len(l1)):
    if l1[i] in l2:
        common.append(l1[i])
    if l1[i] not in l2:
        unique.append(l1[i])
for i in range(0, len(l2)):
    if l2[i] not in l1:
        unique.append(l2[i])

print(f"unique: {unique}\ncommon: {common}")

        