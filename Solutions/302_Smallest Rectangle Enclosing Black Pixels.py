"""
Keys:
- The most intuitive for this question should be BFS / DFS, cause there is only one connection component of "1", traverse
  would not be complicated. However, in the worst case, this cost O(m*n) time, while the question ask for a solution 
  better than O(m*n).
- Notice that we could perform Binary Search for this question. The time complexity would be better than O(m*n).

Complexity:
Time: O(n*logm + m*logn)
Space: O(1)
"""


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        top = bottom = left0 = right0 = 0

        # Find top. (Last row without 1)
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if "1" in image[mid]:
                right = mid - 1
            else:
                left = mid + 1
        top = right

        # Find bottom. (Last row with 1)
        left, right = x, m - 1
        while left <= right:
            mid = left + (right - left) // 2
            if "1" in image[mid]:
                left = mid + 1
            else:
                right = mid - 1
        bottom = right

        # Find left. (Last column without 1)
        left, right = 0, y
        while left <= right:
            mid = left + (right - left) // 2
            haveOne = False
            for i in range(m):
                if image[i][mid] == "1":
                    haveOne = True
                    break
            if haveOne:
                right = mid - 1
            else:
                left = mid + 1
        left0 = right

        # Find right. (Last column with 1)
        left, right = y, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            haveOne = False
            for i in range(m):
                if image[i][mid] == "1":
                    haveOne = True
                    break
            if haveOne:
                left = mid + 1
            else:
                right = mid - 1
        right0 = right
        return (bottom - top) * (right0 - left0)
