"""
Given an array of size n, find the majority element.
The majority element is the element that appears more
than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the
majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

def majority_element(nums):
    l = len(nums)
    if l == 1:
        return nums[0]
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    for num in nums:
        if d[num] > (l//2):
            return num

print(majority_element([2,2,1,1,1,2,2]))