a = {1,2,3,4,5}
b = {4,3,2,5,9}

# empty set look like set() instead of {}(dictionary)

print(a|b)
print(a.union(b))
a.update(b) # update in a set

print(a&b)
print(a.intersection(b))
a.intersection_update(b)
print(a)

print(a-b)
print(a.difference(b))
print(a.difference_update(b))
print(a)

print(a^b)
print(a.symmetric_difference(b))
print()

