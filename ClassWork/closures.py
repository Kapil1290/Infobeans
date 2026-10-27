import time

def dec_performance(fun):
    def check():
        start = time.perf_counter()
        fun()
        end = time.perf_counter()
        print(end-start)
    return check

@dec_performance
def check_1000():
    return sum(1000)

@dec_performance
def check_10000():
    return sum(10000)

check_1000()

check_10000()