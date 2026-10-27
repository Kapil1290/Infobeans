#1
def reverse_str(string):
    i = 0
    j = len(string)-1
    string = list(string)
    while i<j:
        string[i],string[j]=string[j],string[i]
        i+=1
        j-=1
    return "".join(string)
name = "kapil"
print(reverse_str(name))



#2
def palindrome(check_string):
    list_demo = list(check_string)
    l = 0
    h = len(check_string)-1
    flag=0
    while l<h:
        while l<h and not list_demo[l].isalnum():
            l+=1
        while l<h and not list_demo[h].isalnum():
            h-=1
        if list_demo[l]!=list_demo[h]:
            flag = 1
            break
        else:
            l+=1
            h-=1
    if flag:
        print("not palindrome")
    else :
        print("palindrome")
# palindrome("khkdfṇ2&%88,2..*hk")

#3
def vowel_and_consonant(check_string):
    vowel=0
    consonant = 0
    check_list = "aeiouAEEIOU"
    list_demo = list(check_string)

    for ch in list_demo:
        if ch in check_list:
            vowel+=1
        elif (ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122):
            consonant+=1
    return vowel,consonant
# vowel, consonant = vowel_and_consonant("kadbdieu495*/-dkfkvc")
# print(f"Vowels: {vowel}\nConsonants: {consonant}")

#4
def dig_num_symb(check_string):
    upper_case = 0
    lower_case = 0
    digit = 0
    special_symbol = 0
    list_demo = list(check_string)

    for ch in list_demo:
        if ord(ch)>=ord("0") and ord(ch)<=ord("9"):
            digit+=1
        elif ord(ch)>=ord("A") and ord(ch)<=ord("Z"):
            upper_case+=1
        elif ord(ch)>=ord("a") and ord(ch)<=ord("z"):
            lower_case+=1
        else:
            special_symbol+=1
    print(f"digit: {digit}\ncapital: {upper_case}\nsmall: {lower_case}\nspecial: {special_symbol}")
# dig_num_symb("kadbdieu495*/-dkfkvc")


#5
def len_of_string(string):
    length = 0
    for i in string:
        length+=1
    print(f"length is: {length}")
# len_of_string("kapilkdifut")


#6
def count_word(sentance):
    sentance = sentance.strip()
    count=0
    i = 0
    word = 0
    while(i<len(sentance)):
        if sentance[i] != " ":
            word=1
        elif word==1:
            word=0
            count+=1
        if sentance[i] != " " and i==len(sentance)-1:
            count+=1
        i+=1
        
    print(count)

# val = " i am kapil prdd dfd sd  ksdk  fdkdsf  ajapat "
# count_word(val)


#7
def upper_conversion(word):
    return word.upper()
# print(upper_conversion("indorE345&"))


#8 
def remove_space(string):
    a = list(string)
    for ch in a:
        if ch==" ":
            a.remove(ch)
    new_str = "".join(a)
    print(new_str)
# remove_space(" my name is kapl ")


#9 
def first_last_digit(string):
    print(f"first character: {string[0]}\nsecond character: {string[len(string)-1]}")
# first_last_digit("kapil") 


#10
def first_last_digit(string):
    string = string.replace(' ',"-")
    print(string)
# first_last_digit("kapil is a boy") 


#11
def check_occurance(string):
    result = {}
    for ch in string:
        result[ch] = result.get(ch, 0)+1
    # print(result)
# check_occurance("addbcca")


#12
def check_equality(a,b):
    s = set()
    s.add(a)
    s.add(b)
    if len(s)>1:
        print("Unequal")
    else:
        print("Equal")
# check_equality("kail","kil")


#13
def char_saperate_line(string):
    for ch in string:
        print(ch)
# char_saperate_line("kapil")


# #14
# def remove_space(string):
#     a = list(string)
#     i=0
#     while i<len(a):
#         if ord(a[i])>=ord(a[i])<=ord("9"):
#             print(a[i])
#             a.remove(a[i])
#         else:
#             i+=1
#     new_str = "".join(a)
#     print(new_str)
# remove_space("kak34s4pi3442l")

#14
def remove_digit(string):
    i=0
    while i<len(string):
        if ord(string[i])>=ord(string[i])<=ord("9"):
            string.remove(string[i])
        else:
            i+=1
# remove_digit("kak34s4pi3442l")

#15
def ascii_value(string):
    for ch in string:
        print(ord(ch))
# ascii_value("ka9") 


#16
def anagram(string,string2):
    res = {}
    for ch in string:
        res[ch] = res.get(ch,0)+1
    for ch in string2:
        res[ch] = res.get(ch,0)-1
        if res[ch]==0:
            del res[ch]
    if not res:
        print("True")
    else:
        print("False")
# anagram("hero", "hore")



#17
def non_repeating(string):
    val=0
    res = {}
    for ch in string:
        res[ch] = res.get(ch,0)+1
    for key,value in res.items():
        if value==1:
            val = key
            break
    if val:
        print(f"character is {val.upper()}")
    else:
        print("No repeating character")
# non_repeating("aabbccddaa")



#18
def non_repeating(string):
    val=0
    res = {}
    for ch in string:
        res[ch] = res.get(ch,0)+1
    for key,value in res.items():
        if value>=2:
            val = key
            break
    if val:
        print(f"character is {val.upper()}")
    else:
        print("No character")
# non_repeating("programming")



#19
def non_repeating(string):
    val=0
    res = {}
    for ch in string:
        res[ch] = res.get(ch,0)+1
    print(res)
# non_repeating("aabbccddaa")


#20
def remove_duplicate(string):
    res = []
    for ch in string:
        if ch not in res:
            res.append(ch)
    string = "".join(res)
    print(string)
# remove_duplicate("programmming")


#21 
def high_repeating(string):
    val=0
    res = {}
    max = -1000000
    for ch in string:
        res[ch] = res.get(ch,0)+1
    for key,value in res.items():
        if value>max:
            max=value
            val = key
    if val:
        print(f"First Highest repeating character is {val.upper()}")
    else:
        print("No character")
# high_repeating("aabbccccd")


#22  not accurate 
def sec_high_repeating(string):
    val=0
    res = {}
    max = -1000000
    for ch in string:
        res[ch] = res.get(ch,0)+1
    for key,value in res.items():
        if value>max:
            max=value
            val = key
    del res[val]
    print(res)
    max = -1000000
    for key,value in res.items():
        if value>max and key != val:
            max=value
            val = key
            break
    if val:
        print(f"Second Highest repeating character is {val.upper()}")
    else:
        print("No character")
sec_high_repeating("aabbccccd")


#23
def reverse_word(string):
    res = []
    res_str = ""
    string = string.strip()
    for idx in range(len(string)-1, -1, -1):
        if string[idx]!=" ":
            res_str+=string[idx]
        elif string[idx]==" " and idx!=0:
            res.append(res_str[::-1]+" ")
            res_str=""
        if idx==0:
            res.append(res_str[::-1])
            res_str=""
        
    print("".join(res))
# reverse_word("python is programming language")
            
#24
def reverse_word(string):
    res = []
    res_str = ""
    string = string.strip()
    for idx in range(0, len(string)):
        if string[idx]!=" ":
            res_str+=string[idx]
        elif string[idx]==" " and idx!=0:
            res.append(res_str[::-1]+" ")
            res_str=""
        if idx==len(string)-1:
            res.append(res_str)
            res_str=""
        
    print("".join(res))
# reverse_word("Python is easy")


#25
def is_digit(string):
    res = []
    for ch in string:
        if ord(ch)>=ord(ch)<=ord("9"):
            res.append(ch)
    if res:
        print(f"Digits are {res}")
    else:
        print("no digit present")
# is_digit("kapdf73il1213")


#26
def longest_word(string):
    max_len=0
    res_str = ""
    word = ""
    string = string.strip()
    for idx in range(0, len(string)):
        if string[idx]!=" ":
            res_str+=string[idx]
        elif string[idx]==" " and idx!=0:
            if max_len<len(res_str):
                word = res_str
                max_len=len(res_str)
            res_str=""
        if idx==len(string)-1:
            
            if max_len<len(res_str):
                word = res_str
                max_len=len(res_str)
            res_str=""
    print(word)
# longest_word("Python is easy but not a toughest")


#27
def dual_freq(string):
    val=0
    res = {}
    result = []
    for ch in string:
        res[ch] = res.get(ch,0)+1
    for key,value in res.items():
        if value>1:
            result.append(f"{key}:{value}")
    if result:
        print(result)
    else:
        print("no anything")
# dual_freq("kdffdk")


#28  Example: "abcd" and "cdab" → True
def circular_str(original, rotated):
    res_str = ""

    for i in range(0,len(original)):
        res = ""
        j=i 
        while j<len(original):
            res += original[j]
            j+=1

            if j==len(original)-1:
                res += original[j]
                j=0
            if j==i:
                break
        if res==rotated:
            print("True")
            break
    else:
        print("False")
circular_str("aeioua", "ouaaei")


#29
def remove_char(string, remove_character):
    string = list(string)
    print(string)
    if remove_character in string:
        for ch in range(0, len(string)):
            if string[ch]==remove_character:
                del string[ch]
                string = "".join(string)
                print(string)
                break
    else:
        print("not found")
    
# remove_char("kdffdk", "f")


#30
def prefix_string(str_list):
    res = []
    for idx_char in range(0, len(str_list[0])):
        mark = False
        for idx in range(1, len(str_list)):
            if str_list[0][idx_char]==str_list[idx][idx_char]:
                mark = True
            else:
                mark = False
                break
        if mark:
            res.append(str_list[0][idx_char])
        else:
            break
    print("".join(res))
# prefix_string(["flower", "flow", "fly"])



#31
def long_substr_no_repeating(string):
    max_len=0
    s = set()
    i,j=0,0
    while(j<len(string)):

        while string[j] in s:
            s.remove(string[i])
            i+=1
        if string[j] not in s:
            s.add(string[j])
            j+=1
        if max_len<len(s):
            max_len=len(s)
            res=string[i:j]
    print(f'Length: {max_len}\nSubstring: {res}')

# long_substr_no_repeating("kapilprajapat")



#32
def long_palindrome_substr(string):
    def is_palindrome(a):
        i=0
        mark = True
        j=len(a)-1
        while(i<=j):
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        if mark:
            return True
    res = []
    val=""
    len_substr = 0
    for i in range(0, len(string)):
        for j in range(i+1, len(string)):
            res.append(string[i:j])
    for word in res:
        if is_palindrome(word) and len(val)<len(word):
            val = word
    print(val)

# long_palindrome_substr("babad")


#33
def bracket_balancing(string):
    i = 0
    j = len(string)-1
    mark = True
    while i<j:
        if string[i]!=string[j]:
            mark = False
            break
        i+=1
        j-=1
    if mark:
        print("True")
    else:
        print("False")
# bracket_balancing("[()]")


#34
def compress_string(string):
    res = {}
    val = []
    char_count=1
    for ch in string:
        res[ch] = res.get(ch,0)+1
    for key,value in res.items():
        val.append(key)
        val.append(str(value))
    print("".join(val))
# compress_string("aabccccd")



#35
def expand_string(string):
    res = []
    i = 0
    while i<len(string):
        if string[i].isdigit():
            print(int(string[i]))
            for j in range(0, int(string[i])):
                res.append(string[i-1])
        i+=1
    print("".join(res))

# expand_string("a2b4c5")



        
