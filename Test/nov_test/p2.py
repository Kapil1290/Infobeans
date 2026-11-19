str1 = "listen"
str2 = "silent"

check_dict = {}
for i in str1:
    check_dict[i] = check_dict.get(i,0)+1

for i in str2:
    check_dict[i] = check_dict.get(i,0)-1



for i in check_dict.values():
    if i!=0:
        print("Not anagram...")
        break
else:
    print("anagram")
    

   

