"""
Given two words word1 and word2, find the minimum
number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""


def minDistance(text1: str, text2: str) -> int:
    if text1==text2:
        return 0
    l1 = len(text1)
    l2 = len(text2)
    dp = [[0 for _ in range(l2+1)] for _ in range(2)]
    # dp[l1-1][l2-1] = 0

    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0:
                dp[i%2][j]=j
            elif j == 0:
                dp[i%2][j]=i
            elif text1[i-1]==text2[j-1]:
                dp[i%2][j]=dp[(i-1)%2][j-1]
            else:
                dp[i%2][j] = 1 + min((dp[(i-1)%2][j-1]), (dp[i%2][j-1]), (dp[(i-1)%2][j]))
    return dp[l1%2][l2]