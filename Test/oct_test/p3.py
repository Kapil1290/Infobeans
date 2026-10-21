demo_list = [33,4,3,2,1,3]

for i in range(0, len(demo_list)):
    max = demo_list[i]
    for j in range(i+1, len(demo_list)):
        if demo_list[i]>demo_list[j]:
            demo_list[i], demo_list[j] = demo_list[j], demo_list[i]
    
print(f"Second larger is: {demo_list[len(demo_list)-2]}")
print(demo_list)