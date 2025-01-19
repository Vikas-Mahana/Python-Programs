#Flatten a Nested List
list = [[1], [2, 3], [4, 5, 6, 7]]
new_list = []
for i in list:
    for j in i:
        new_list.append(j)
print(new_list)