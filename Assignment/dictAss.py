
'''
#1
dic = {
    "name":"kapil",
    "age":23,
    "marks":88
}

for i in dic.items():
    print(i)

print("\n")

#2
for key, value in dic.items():
    print(f"{key}\t{value}")


#3

if "name" in dic:
    print("present") 
else:
    print("Not present")

#4 
dic["city"]="Indore"
print(dic)


#5
dic["marks"]=78
print(dic)

#6
key = "a"
if key in dic :
    dic.pop(key)
else:
    print("key not found")


#7
count=0
for i in dic.items():
    count+=1
print(count)


#8
sum= 0
for key, value in dic.items():
    a =  str(value)
    if a.isdigit():
        sum+=value
print(sum)

#9
max=float('-inf')
for key, value in dic.items():
    a =  str(value)
    if a.isdigit():
        a = int(a)
        if max<a:
            max=a 
            sum = key  
print(sum)

#10
dict1 = {
    "name":"kapil",
    "age":34,
    "city":"indore"
}
dict2 = {
    "name":"ram",
    "mob":3343348557,
    "gender":"male"
}
newdict = dict1 | dict2
print(newdict)


#11
keys = ["name", "age", "city"]
values = ["kapil", 34, "indore"]
res = {}
idx=0
if len(keys)!=len(values):
    print("can't create the dictionary")
else:
    for i in range(0, len(keys)):
        res[keys[i]] = values[i]
print(res)


#12
for key,value in newdict.items():
    print(f"{key}\t \t {value}")
print("\n")
for key,value in newdict.items():
    print(f"{key}:{value}")
print("\n")


#13
res = {3:3}
if res=={}:
    print("Dictionary is empty")
else:
    print("not empty")


#14  changes also perform in the original variable when we copied normally
students = {
    "std1":{
        "name":"kapil",
        "age":23,
        "marks":{
            "other":88,
            "softskills":75,
            "technical":56
        }
    },
    "std2":{
        "name":"ram",
        "age":23,
        "marks":{
            "other":96,
            "softskills":56,
            "technical":80
        }
    }
}
new_var = students
new_var["std1"]["marks"] = {
            "math":88,
            "english":75,
            "chemistry":56
        }
print(students)



#15
result = {}
# {result[]=i*i for i in range(1, 6)}
for i in range(1,6):
    result[i]=i*i
print(result)



#16
value = "kapilkfkkdsfd"
result={}
for char in value:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
print(result)



#17
value = [1,2,2,3,4,4,5]
result={}
for val in value:
    if val in result:
        result[val] += 1
    else:
        result[val] = 1
print(result)


#18
res = {'k': 4, 'f': 2, 'd': 2, 's': 1}
maxoccur = float('inf')   # positive infinite value 
for key,value in res.items():
    if value<maxoccur:
        maxoccur=value
        identityofkey=key

print(f"character {identityofkey} has {res.get(identityofkey)} less occurance")
print("\n")


#19
value = [1,2,5]
result={}
res = []
for val in value:
    if val in result:
        result[val] += 1
    else:
        result[val] = 1
print(f"Frequencies of key is:- {result}")
for key,value in result.items():
    if value>1:
        res.append(key)
if res == []:
    print("No repeated char")
else:
    print(res)



#20
student = {
    "name":"kapil",
    "age":23,
    "gender":"male",
    "add":"indore"
}
print({ value:key for key,value in student.items() })


#21
d1 =  {'a': 10, 'b': 20}
d2 = {'b': 5, 'c': 7}

for key, value in d2.items():
    if key in d1:
        d1[key] = d1.get(key, 0) +value
    else:
        d1.setdefault(key, 1)
print(d1)


#22
d1 =  {'a': 10, 'b': 20, 'd':2}
print(d1)
d2 = {'b': 5, 'c': 7, 'd':3}
common_keys = []
[common_keys.append(key) for key in d2.keys() if key in d1]

# for key in d2.keys():
#     if key in d1:
#         common_keys.append(key)
print(common_keys)

'''

#23
list_demo = {
    "id1":23,
    "id2":30,
    "id3":22,
    "id4":88,
    "id5":75
}
result={}
key_val = 0
min = 10000000
for _ in range(len(list_demo)):
    min=100000
    for key,value in list_demo.items():
        if min>value:
            min=value
            key_val=key
    result[key_val]=min
    del list_demo[key_val]
print(result)

    
   


#24
item_list = ["cat", "apple", "dog", "mango"]
print({len(word):[i if len(word)==len(i) else "" for i in item_list] for word in item_list})
print("\n\n")


#25
students = {
    "std1":{
        "name":"kapil",
        "age":23,
        "marks":{
            "other":88,
            "softskills":75,
            "technical":56
        }
    },
    "std2":{
        "name":"ram",
        "age":23,
        "marks":{
            "other":96,
            "softskills":56,
            "technical":80
        }
    },
    "std3":{
        "name":"mohan",
        "age":33,
        "marks":{
            "other":55,
            "softskills":74,
            "technical":45
        }
    }
}
sum = 0
max_marks = float('-inf')
for detail in students.values():
    sum = 0
    for mark in detail['marks'].values() :
        sum += mark
    if sum >max_marks:
        max_marks=sum
        topper = detail["name"]
    print(f"Total Marks of {detail["name"]} :- {sum}")
print(f"topper is {topper}")



#26
demo_dict = {
    "value1":34,
    "value2":45,
    "value3":44,
    "value4":77
}
res = []

for value in demo_dict.values():
    res.append(value)
res.sort()
print(res[len(res)-2])



print("\n")
#27
data_list = ["eat", "tea", "bat", "ate", "potato", "naman", "anman"]
res = {}
for word in data_list:
    val = "".join(sorted(word))
    if val in res:
        res[val].append(word)
    else:
        res[val] = [word]
print(list(res.values()))


print("\n")

#28




print("\n")
#29
same_value_list = []
d1 = {"name":"kapil", "age":33, "city":"indore", "mob":895686743}
d2 = {"name":"ram", "age":33, "city":"devas"}
if len(d1)>len(d2):
    for key,value in d1.items():
        if key in d2 and d2[key]==value:
            same_value_list.append(key)
print(same_value_list)
'''
#30
students = {
    "std1":{
        "name":"kapil",
        "age":23,
        "marks":{
            "other":88,
            "softskills":75,
            "technical":56
        }
    },
    "std2":{
        "name":"ram",
        "age":23,
        "marks":{
            "other":96,
            "softskills":56,
            "technical":80
        }
    },
    "std3":{
        "name":"mohan",
        "age":33,
        "marks":{
            "other":55,
            "softskills":74,
            "technical":45
        }
    }
}

search_key = "marks"
val=0
for key,value in students.items():
    if(key == search_key) or (search_key in value):
        val = key 
        break
if val:
    print("Key founded")
else:
    print("key not founded")




#31 
#Output of question is :- {'a':99, 'b':20, 'c':30}
data = {"a": 10, "b": 20}
data["c"] = 30
data["a"] = 99


#32
data = {"x": 1, "y": 2}
print(data.get("z"))    # will give None if key not present

#33
#print(data["z"]) # will give KEY ERROR!!!!!!!!!

#34
data = {"name":"kapil", "age":23}
data_new = data
data_new["name"]="ram"
# o/p will also update the data dictionary because the concept of shallow copy
print(data)


#35
data = {"a": 1, "b": 2}
data.update({"b": 5, "c": 3})
# combine the o/p with all data
print(data)

'''

