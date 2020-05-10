"""
In a town, there are N people labelled from 1 to N.
There is a rumor that one of these people is secretly
the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b]
representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of
the town judge.  Otherwise, return -1.
"""


def find_judge(n, trust):
    if n == 1 and not trust:
        return 1
    non_judge = {}
    judge = {}

    for t in trust:
        non_judge[t[0]] = 1
        judge[t[1]] = judge.get(t[1], 0) + 1
        if t[0] in judge:
            del judge[t[0]]
        if t[1] in judge:
            if t[1] in non_judge:
                del judge[t[1]]

    if not judge:
        return -1
    elm = judge.popitem()
    if elm and not judge:
        if elm[1] == n-1:
            return elm[0]
    return -1

print(find_judge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))


