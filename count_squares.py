"""
Given a m * n matrix of ones and zeros, return how
many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
"""

def count_squares(matrix):
    row = len(matrix)
    col = len(matrix[0])
    if row == 0:
        return 0

    new_matrix = [[0]*(col+1) for _ in range(row+1)]
    total = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==1:
                new_matrix[i][j]+=min(new_matrix[i][j-1],new_matrix[i-1][j],new_matrix[i-1][j-1])+1
                total+=new_matrix[i][j]
    return total

m = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(count_squares(m))