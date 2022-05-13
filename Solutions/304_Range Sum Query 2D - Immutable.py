"""
Keys:
- Each row is a unit to perform prefix sum. The sumRegion is a operation where We would add sum of subarrays a lot.
  Therefore, we should notice that this is a question to use prefix sum.

Complexity:
Time: O(m)
Space: O(mn)
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(1, len(matrix[i])):
                matrix[i][j] += matrix[i][j-1]
        self.matrix = matrix.copy()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row1, row2+1):
            result += self.matrix[i][col2] - \
                (self.matrix[i][col1-1] if col1 > 0 else 0)
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# This question has a more efficient solution. Not gonna cover that in this solution.
