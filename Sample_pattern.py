"""
Create a function named pattern which takes an integer as an
input and print the following pattern.

10 20 30 40 50
"""


def pattern(n):
    i = 1
    num = 10
    while i <= n:
        print(num, end=" ")
        num = num + 10
        i = i + 1
    print()


pattern(5)



"""
Create a function named pattern which takes an integer as 
an input and print the following pattern.

1 2 4 8 ...
"""


def pattern(n):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = num * 2
        i = i + 1
    print()


pattern(10)



"""
Don't create a function, just print the following pattern
1  11  111  1111  11111....n times (Ask n from user)
"""


def pattern(n):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = (num * 10) + 1
        i = i + 1
    print()


# You can even directly ask number as given below
# Although it is not recommended but still you can.

# Best way is to ask input and store it in a variable
# and pass that variable to the function
pattern(int(input("Enter a number = ")))