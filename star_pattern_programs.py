"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

def pattern(n):
    for i in range(1, n+1):
        for _ in range(1, (n+1)-i):
            print(" ",end=" ")
        for _ in range(1, i+1):
            print("*", end=" ")
        print()
    
pattern(5)

"""
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5
"""

def pattern(n):
    for i in range(1, n+1):
        for _ in range(1, (n+1)-i):
            print(" ",end=" ")
        for _ in range(1, i+1):
            print(i, end=" ")
        print()
    
pattern(5)


"""
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5 
"""

for i in range(5, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(i, 6):
        print(k, end=" ")
    print()

"""
       * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
"""

for i in range(1,6):
    for j in range(1, 6-i):
        print(" ", end=" ")
    for k in range(1,(2*i-1)+1):
        print('*', end=" ")
    print()