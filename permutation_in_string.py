"""
Given two strings s1 and s2, write a function to return
true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is
the substring of the second string.
"""

from collections import Counter
def checkInclusion(s1: str, s2: str):
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len==0 or s2_len==0:
        return False

    if s2_len<s1_len:
        return False

    s1_counter = Counter(s1)
    s2_counter = Counter()

    for index, c in enumerate(s2):
        s2_counter[c]+=1

        if index >= s1_len:
            if s2_counter[s2[index-s1_len]] == 1:
                del s2_counter[s2[index-s1_len]]
            else:
                s2_counter[s2[index - s1_len]] -= 1

        if s1_counter==s2_counter:
            return True
    return False

print(checkInclusion("ab","eidboaoo"))
