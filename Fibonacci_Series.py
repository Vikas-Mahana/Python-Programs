# Fibonacci series
def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b

for i in fibo(10):
    print(i)