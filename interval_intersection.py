"""
Given two lists of closed intervals, each list of
intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes
the set of real numbers x with a <= x <= b.  The intersection
of two closed intervals is a set of real numbers that is either
empty, or can be represented as a closed interval.  For example,
the intersection of [1, 3] and [2, 4] is [2, 3].)
"""

def interval_intersection(A,B):
    result = []
    a_len = len(A)
    b_len = len(B)

    a_ptr = b_ptr = 0

    while a_ptr < a_len and b_ptr < b_len:
        start, end = max(A[a_ptr][0], B[b_ptr][0]), min(A[a_ptr][1], B[b_ptr][1])
        if start <= end:
            result.append([start, end])

        if A[a_ptr][1] < B[b_ptr][1]:
            a_ptr += 1
        else:
            b_ptr += 1

    return result