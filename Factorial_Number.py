# Factorial of a number
def fact(n):
    f = 1
    for i in range(2,n+1):
        f *=i
    return f
fact(4)