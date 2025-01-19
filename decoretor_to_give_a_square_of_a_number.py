# Write a decoretor to give a square of anumber.
def perfect_square(str_param):
    def middle_decorator(func):
        def inner(x):
            return func(x)
        return inner
    return middle_decorator

@perfect_square('Find the square')
def display_square(a):
    return a*a

display_square(2)