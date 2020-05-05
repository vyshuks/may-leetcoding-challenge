"""
Given a string, find the first non-repeating character
in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import  OrderedDict

def first_uniq_char(s):
    """
    Return first unique character
    :param s: str
    :return: int
    """
    d = OrderedDict()
    for c in s:
        d[c] = d.get(c, 0) + 1

    print(d)
    for i,c in enumerate(s):

        if d[c] == 1:
            return i
    return -1

print(first_uniq_char("dddccdbba"))