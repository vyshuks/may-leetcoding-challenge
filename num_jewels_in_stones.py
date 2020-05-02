"""
You're given strings J representing the types of
stones that are jewels, and S representing the stones
you have.  Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters
in J and S are letters. Letters are case sensitive, so "a" is
considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
"""

def num_jewels_in_stones(J,S):
    """
    Retuen jewels count
    :param J: str - stones
    :param S:
    :return:
    """
    jewels = {}
    for jewel in J:
        jewels[jewel]=1

    jewels_count = 0
    for stone in S:
        if stone in jewels:
            jewels_count+=1
    return  jewels_count

print(num_jewels_in_stones("z", "ZZ"))