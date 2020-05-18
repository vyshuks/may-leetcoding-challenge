"""
Given a string s and a non-empty string p, find all
the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and
the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
from collections import Counter
def find_anagrams(s, p):
    s_length = len(s)
    p_length = len(p)
    result = []
    if s_length == 0:
        return result
    if p_length > s_length:
        return result

    char_count_p = Counter(p)
    char_count_s = Counter()

    for index, c in enumerate(s):
        char_count_s[c]+=1
        if index >= p_length:
            if char_count_s[s[index-p_length]] == 1:
                del char_count_s[s[index-p_length]]
            else:
                char_count_s[s[index-p_length]] -= 1

        if char_count_p == char_count_s:
            result.append(index-p_length+1)

    return result

print(find_anagrams("abab","ab"))





