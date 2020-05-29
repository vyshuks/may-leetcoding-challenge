"""
Given a set of N people (numbered 1, 2, ..., N),
we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should
not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed
to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone
into two groups in this way.
"""
from collections import defaultdict

def possible_bipartition(N, dislikes):
    graph = defaultdict(list)
    groups = [-1]*N
    for a, b in dislikes:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    def dfs(v1, grp):
        print(v1)
        if groups[v1] == -1:
            groups[v1] = grp
        else:
            return groups[v1] == grp

        for n in graph[v1]:
            # print(grp)
            if not dfs(n, 1-grp):
                return False
        return True

    for i in range(N):
        if groups[i] == -1 and not dfs(i,0):
            return False

    return True

print(possible_bipartition(4, [[1,2],[1,3],[2,4]]))







