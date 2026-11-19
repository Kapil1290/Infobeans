lam = lambda a,b:a+b 
print(lam(2,3))

lam = (lambda a,b:a-b)(34,22)
print((lambda a,b:a-b)(34,22))

# anonymous(No name) class use for small operation and it return value automatically



l = [2,3,33,54]
def inc(x):
    return x*x
new_list = list(map(inc,l))    # here we are passing function reference and map return map class object


new_list = list(map(lambda a: 2+a,l))
print(new_list)