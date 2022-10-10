# Count the repeted charaters in a given string.
string = 'aabbbcccddddeeeee'
d = {}
for i in string:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1
print(d)
for i,j in d.items():
    print('{}{}'.format(i,j),end='')