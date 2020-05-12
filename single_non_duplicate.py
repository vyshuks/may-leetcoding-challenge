"""
You are given a sorted array consisting of only integers
where every element appears exactly twice, except for one
element which appears exactly once. Find this single element
that appears only once.
"""

def single_non_duplicate(nums):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = (start+(end))//2
        print(mid)

        is_even_half = (end-mid) % 2 == 0
        if mid == end or mid == start:
            return nums[mid]

        if nums[mid]==nums[mid+1]:
            if is_even_half:
                start = mid+2
            else:
                end = mid-1
        elif nums[mid]==nums[mid-1]:
            if is_even_half:
                end = mid-2
            else:
                start = mid+1
        else:
            return nums[mid]
    return nums[start]

print(single_non_duplicate([1,1,2]))