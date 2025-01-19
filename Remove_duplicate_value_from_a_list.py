#remove duplicate value from a list
  my_list = ('a','b','c','b','n','z','n')
l = []
for i in my_list:
    if i not in l:
        l.append(i)
print(l)