# printing highest even number of a given list
def highest_even(li):
    li2 = []
    for i in li:
        if i % 2 == 0:
            li2.append(i)
    return max(li2)

highest_even([10,2,5,4,8,11])