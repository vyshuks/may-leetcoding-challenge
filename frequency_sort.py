"""
Given a string, sort it in decreasing order based
on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore
"eetr" is also a valid answer.
"""

from collections import Counter
def frequency_sort(s):
    c = Counter(s)
    result = []
    for char in c.most_common():
        result.append(char[0]*char[1])
    return "".join(result)

print(frequency_sort("tree"))
