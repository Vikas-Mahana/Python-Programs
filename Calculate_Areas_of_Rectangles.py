'''
Consider a rectangular surface with n rows and columns. The width of the columns are
A1,A2,...,An centimeters and the height of the rows are B1,B2,...,Bn centimeters. The
rectangle is divided into n × n smaller rectangles. Let the column and row numbers be i, j
respectively. Each intersection of column i and row j is assigned a number from the
following set [0, 1, 2] given by the formula ( i + j ) mod 3 for all 1 ≤ i, j ≤ n. Calculate the
cumulative area of all the rectangles with number 0, 1 & 2.
Input 
The input consists of the following integers: On the first line: the integer n, 
On the second line: the values of A1,...,An, n integers separated by single
spaces,
On the third line: the values of B1,...,Bn, n integers separated by single spaces.
Limits
The input satisfies 3 ≤ n ≤ 100000 and 1 ≤ A1,...,An,B1,...,Bn ≤ 10000.
Output
The output should consist of three integers separated by single spaces, representing the
total area for each number 0, 1 and 2. 
'''

def countArea(rows, col):
  count0 = 0
  count1 = 0
  count2 = 0

  for i in range(0,len(rows)): 
    for j in range(0,len(col)):
      rectNum = (i + j) % 3
      area = rows[i] * col[j]
      if (rectNum == 0): 
        count0 += area
      elif (rectNum == 1): 
        count1 += area
      elif (rectNum == 2): 
        count2 += area
  print(count0, count1, count2)


countArea([3, 3, 3], [3, 3, 3])