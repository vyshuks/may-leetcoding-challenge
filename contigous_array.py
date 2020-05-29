"""
Given a binary array, find the maximum length of a
contiguous subarray with equal number of 0 and 1.
"""


from typing import List
def findMaxLength(nums: List[int]) -> int:
    s = 0
    max_length = 0
    d = {}
    for i, num in enumerate(nums):
        num = -1 if num == 0 else 1
        s = s + num
        if s == 0:
            max_length = i + 1
        if s in d:
            if max_length < (i - d[s]):
                max_length = (i - d[s])
        else:
            d[s] = i
    return max_length