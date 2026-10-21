demo_list = [12, 45, 7, 45, 30, 22, 30]

for i in range(0, len(demo_list)):

    for j in range(i+1, len(demo_list)):

        if demo_list[i]>demo_list[j]:
            demo_list[i], demo_list[j] = demo_list[j], demo_list[i]
    
for i in range(len(demo_list)-2, -1, -1):
    if demo_list[i]!=demo_list[i+1]:
        print(f"Second larger is: {demo_list[i]}")
        break
