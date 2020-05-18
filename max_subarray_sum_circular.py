"""
Given a circular array C of integers represented by A,
find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects
to the beginning of the array.  (Formally, C[i] = A[i]
when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A
at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there
does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
"""

def max_subarray_sum(A):

    max_end = 0
    max_so_far = None
    min_end = 0
    min_so_far = None
    total_sum = 0
    for num in A:
        total_sum += num
        max_end = max(max_end+num, num)
        max_so_far = max(max_end, max_so_far) if max_so_far else max_end
        min_end = min(min_end+num, num)
        min_so_far = min(min_end, min_so_far) if min_so_far else min_end
    return max(max_so_far, total_sum-min_so_far) if max_so_far > 0 else max_so_far


print(max_subarray_sum([-2,-3,-1]))