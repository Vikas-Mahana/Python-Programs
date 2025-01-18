"""Find Fectors of number."""

def find_fectors(num: int):
    i = 1
    fectors = []
    while i <= num:
        if num % i == 0:
            fectors.append(i)
        i+=1
    print(fectors)

find_fectors(12)
