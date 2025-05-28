"""Take Input form User and Reverse a String (without using built-in functions)"""

def reverse_string(s):
    result = ''
    for char in s:
        result = char + result
    print(result)
user_input = input("Enter a String: ")

reverse_string(user_input)