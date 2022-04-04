"""
Keys:
- A typical Topological Sorting problem.

Complexity:
Time: O(V + E)
Space: O(V + E)
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        connections = collections.defaultdict(list)

        for course, pre in prerequisites:
            indegrees[course] += 1
            connections[pre].append(course)
        courseOrder = []

        while True:
            haveIndegreeZero = 0
            for i in range(numCourses):
                if indegrees[i] == 0:
                    indegrees[i] = -1
                    haveIndegreeZero = 1
                    courseOrder.append(i)
                    for course in connections[i]:
                        indegrees[course] -= 1
            if haveIndegreeZero == 0:
                break

        return courseOrder if len(courseOrder) == numCourses else []
