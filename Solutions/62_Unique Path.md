```
Complexity:
Time: O(mn)

Code:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]
```
