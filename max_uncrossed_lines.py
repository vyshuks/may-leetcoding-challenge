"""
We write the integers of A and B (in the order they are given)
 on two separate horizontal lines.

Now, we may draw connecting lines: a straight
line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other
connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even
at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.
"""

def max_uncrossed_line(A,B):
    len_a = len(A)
    len_b = len(B)

    dp = [[0] * (len_b+1) for _ in range(len_a+1)]

    for i in range(len_a):
        for j in range(len_b):
            if A[i] == B[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return dp[len_a][len_b]