"""
Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is
the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
"""

def remove_k_digits(nums, k):
    if len(nums) == k:
        return "0"

    stack = []
    remove_num= k
    for num in nums:
        while remove_num and stack and stack[-1] > num:
            stack.pop()
            remove_num-=1
        stack.append(num)

    ans = "".join(stack[0:len(nums)-k]).lstrip("0")
    return ans if ans else "0"

print(remove_k_digits("1432219", 3))