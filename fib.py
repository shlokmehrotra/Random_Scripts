#simple fib calculator. Can be solved in O(1) w/ binet's formula
#before optimization O(2^n)
def fib_before(n):
    if n == 1 or n == 2:
        return 1
    return fib_before(n-1) + fib_before(n-2)

#memoization O(n)
def fibonacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    memo[n] =  fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
num = int(input("what term?"))
print(str(fibonacci(num)))