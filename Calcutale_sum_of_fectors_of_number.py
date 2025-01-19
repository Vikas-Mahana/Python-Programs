"""
Create a function that takes two inputs: a range limit and a divisor. 
The function should sum all numbers from 1 to the specified range limit (inclusive) that are divisible by the divisor and return the total sum.
"""

def sum_of_fectors(range_limit: int, divisor:int):
    i = 1
    total = 0
    while i <= range_limit:
        if i % divisor == 0:
            print(i, end=" ")
            total+=i
        i+=1
    print(total)

sum_of_fectors(30, 6)