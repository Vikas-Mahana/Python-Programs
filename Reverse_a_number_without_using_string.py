"""
Write a function that will take number and return the reverse of that number.
"""

def reverse(num: int):
    n = num
    result = 0
    while n > 0:
        last_digit = n % 10
        result = (result * 10) + last_digit
        n = n // 10
    return result

print(reverse(123))
        
