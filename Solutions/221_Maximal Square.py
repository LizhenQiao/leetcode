"""
Keys:
- DP

Complexity:
Time: O(m * n)
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxs = 0
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            if matrix[i][0] == "1":
                maxs = 1
                break
        if maxs == 0:
            for j in range(n):
                if matrix[0][j] == "1":
                    maxs = 1
                    break

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = str((min(int(matrix[i-1][j-1]), int(matrix[i][j-1]),
                                   int(matrix[i-1][j]))) + 1) if matrix[i][j] == "1" else "0"
                maxs = max(maxs, int(matrix[i][j]) ** 2)

        return maxs
