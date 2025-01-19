# reverse word of a given string.
str = "my name is vikas maharana"
a1 = str.split()
l = len(a1)-1
result = []
# using while loop
while l>=0:
    result.append(a1[l])
    l = l-1
print(' '.join(result))

# using for loop
for i in a1:
    if l>=0:
        result.append(a1[l])
        l = l-1
print(' '.join(result))

# using slicing
s1 = str.split()[::-1]
print(' '.join(s1))