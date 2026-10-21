
l1 = [10,20,20,30,40,50]
l2 = [30, 40, 60, 70]
unique=set()
common = set()


for i in range(0, len(l1)):
    if l1[i] in l2:
        common.add(l1[i])
    if l1[i] not in l2:
        unique.add(l1[i])

for i in range(0, len(l2)):
    if l2[i] not in l1:
        unique.add(l2[i])

print(f"unique: {unique}\ncommon: {common}")

        