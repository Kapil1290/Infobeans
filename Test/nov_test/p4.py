str1 = "aaabbbxccd"
ans = []

print(len(ans))
i = 1
count=1

for i in range(0,len(str1)-1):
    if str1[i] not in ans:
        ans.append(str1[i])

    if str1[i]==str1[i+1]:
        count+=1
    else:
        ans.append(str(count))
        count=1
    
    if i==len(str1)-2 and str1[i+1] not in ans:
        ans.append(str1[i+1])
        ans.append("1")


print(ans)


    
    


ans = "".join(ans)
print(ans)