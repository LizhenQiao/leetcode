"""
Complexity:
Time: O(m*n)
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def expand(y, x, color):
            if not 0 <= y < m or not 0 <= x < n or image[y][x] != self.originalColor:
                return None
            image[y][x] = color
            expand(y-1, x, color)
            expand(y+1, x, color)
            expand(y, x-1, color)
            expand(y, x+1, color)

        m = len(image)
        n = len(image[0])
        self.originalColor = image[sr][sc]

        if newColor == self.originalColor:
            return image

        expand(sr, sc, newColor)

        return image
