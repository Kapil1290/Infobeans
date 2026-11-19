# import time

# def dec_performance(fun):
#     def check():
#         start = time.perf_counter()
#         fun()
#         end = time.perf_counter()
#         print(end-start)
#     return check

# @dec_performance
# def check_1000():
#     return sum(1000)

# @dec_performance
# def check_10000():
#     return sum(10000)

# check_1000()

# check_10000()

def decorator(fun):
    def inner(a,b):
        print(a)
        fun(a,b)
        print(b)
    return inner

@decorator
def add(a,b):
    print(a+b)
add(2,3)



def adminrole(role):
    def login():
        print("login done")
        role()
    if role != "User":
        return login

@adminrole
def loginadmin():
    print("Admin LoggedIn")

loginadmin()


import time
import random
from functools import wraps

def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    # Try running the function
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed with error: {e}")
                    
                    # If we've reached the maximum attempts, raise the final exception
                    if attempts == max_attempts:
                        print("Max attempts reached. Raising exception...")
                        raise
                    
                    # Optional: wait a moment before trying again
                    # time.sleep(1)
            
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_network_call():
    if random.random() < 0.8:
        raise ConnectionError("Failed to connect!")
    return "Success!"

print(unstable_network_call())