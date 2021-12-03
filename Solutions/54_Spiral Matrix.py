"""
Keys:
transformation of directions and index

Complexity:

Time: O(m*n)
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        index = 0

        result.append(matrix[0][0])
        matrix[0][0] = None
        x = y = 0

        while True:
            nextx = x + directions[index][0]
            nexty = y + directions[index][1]
            if not 0 <= nextx < n or not 0 <= nexty < m or matrix[nexty][nextx] == None:
                index = (index + 1) % 4
                nextx = x + directions[index][0]
                nexty = y + directions[index][1]
                if not 0 <= nextx < n or not 0 <= nexty < m or matrix[nexty][nextx] == None:
                    break
            result.append(matrix[nexty][nextx])
            matrix[nexty][nextx] = None
            x, y = nextx, nexty

        return result
