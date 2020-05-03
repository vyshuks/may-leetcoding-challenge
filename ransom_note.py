"""
Given an arbitrary ransom note string and another string
containing letters from all the magazines, write a function
that will return true if the ransom note can be constructed
from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once
in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
from collections import defaultdict

def can_construct_ransom_note(ransomNote, magazine):
    """
    check can construct ransom note
    :param ransomNote: str
    :param magazine: str
    :return: bool
    """
    d = defaultdict(int)
    for m in magazine:
        d[m]+=1

    for r in ransomNote:
        if d[r] > 0:
            d[r]-=1
        else:
            return False

    return True
