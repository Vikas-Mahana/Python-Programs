"""
print below pattern.
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1
"""

def pattern(n):
    for i in range(n, 0, -1):
        for j in range(n, i-1,-1):
            print(j, end=" ")
        print()

pattern


"""
print below pattern.
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
"""

def pattern(n):
    for i in range(1, n+1):
        for j in range(i, 1, -1):
            print(j, end=" ")
        print()

pattern(5)