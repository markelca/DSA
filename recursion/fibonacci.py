# 1 2 3 5 8 13 21
# fib(5) = 3 + 2
# fib(5) = fib(5-1) + fib(5-2)

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(7))
