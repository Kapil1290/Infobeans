x = 576
y = 576
print(x is y)

print(None==True)

tup = (2,3,4,[1,22,33,90])
print(tup)


l = ["ant", "dnd", 'thfer', "343gt"]

res = {len(ele):[i if len(i)==len(ele) else "" for i in l] for ele in l}
print(res)


result = {len(ele):[] for ele in l}

x = {}
for ele in l:
    key = len(ele)
    if key in x:
        

print(result)