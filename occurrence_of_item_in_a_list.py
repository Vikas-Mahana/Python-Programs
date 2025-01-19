# occurrence of item in a list
list1 = [1,1,2,1,2,5,3,4,8,4]
result = {}
for i in list1:
    if i in result.keys():
        result[i] +=1
    else:
        result[i] = 1
print(result)