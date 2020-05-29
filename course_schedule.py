"""
There are a total of numCourses courses you have
to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to
take course 0 you have to first take course 1, which is
expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite
pairs, is it possible for you to finish all courses?
"""

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, pre_course in prerequisites:
            adj[course].append(pre_course)

        visited = [0] * numCourses

        def dfs(v):
            if visited[v] == 1:
                return False
            visited[v] = 1
            for d in adj[v]:
                if not dfs(d):
                    return False

            visited[v] = 2
            return True

        for i in range(numCourses):
            if visited[i] == 0 and not dfs(i):
                return False
        return True