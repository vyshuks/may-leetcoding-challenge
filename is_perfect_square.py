"""
Given a positive integer num, write a function which
returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt
"""

def is_perfect_square(num):
    if num==1:
        return True
    start = 1
    end = num
    while start <= end:
        mid = (start+end)//2
        sqr = mid*mid
        if sqr==num:
            return True
        elif sqr > num:
            end = mid-1
        else:
            start = mid+1
    return False

print(is_perfect_square(104976))