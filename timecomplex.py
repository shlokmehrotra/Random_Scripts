import time
start = time.time()

def timetest(n):
    if n < 2:
        return n
    timetest(n-1)
    timetest(n-1)
n = int(input("val"))
print(timetest(n))
end = time.time()
print("time", end - start)