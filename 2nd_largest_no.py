"""
Find the Second Largest Number in a List
"""

def second_largest(lst:list):
    sort_lst = sorted(lst)
    print(sort_lst[-2])

lst = [1,2,4,5,3]

second_largest(lst)