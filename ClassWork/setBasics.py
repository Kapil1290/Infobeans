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
print(a)


s1 = {3,4,5,2,3,10}
print(s1.remove(10))  # does not return anything but return error when element not found 
print(s1)
s1.discard(10) # does not return anything but it does not return error if element not found 
print(a)


