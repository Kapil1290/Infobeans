str1 = "abcabcvkv"
str1 = list(str1)
i = 0
j=0
lenght = 0
ans = []

while(j<len(str1)):
    if str1[j] not in ans:
        ans.append(str1[j])
        j+=1
    else:
        ans = str1[i:j]
        if lenght<len(ans):
            lenght = len(ans)
            tem = str(ans)
            
        while str1[j] in ans:
            ans.pop(0)
            i+=1
        if str1[j] not in ans:
            j+=1
print(f"Longest substring with length {lenght} with string {tem}")

