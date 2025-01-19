# find common element form two list.
a = [3,4,6,8,9]
b = [3,14,15,16,6]
new  = set(a)
another = set(b)
if new&another:
    print(new & another)
else:
    print('no common')