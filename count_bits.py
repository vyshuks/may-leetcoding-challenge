"""
Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary
representation and return them as an array.
"""


def countBits(num: int):
    result = [0]
    for i in range(1, num + 1):
        result.append(result[i >> 1] + int(i & 1))
    return result