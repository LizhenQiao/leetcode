"""
Keys:
- Binary Search.
"""


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def getDivideParts(sweetValue):
            parts = 0
            restSweet = sweetValue
            for s in sweetness:
                restSweet -= s
                if restSweet <= 0:
                    restSweet = sweetValue
                    parts += 1

            return parts

        left = 1
        right = sum(sweetness)

        while left <= right:
            mid = left + (right - left) // 2
            n = getDivideParts(mid)
            if n >= k+1:
                left = mid + 1
            else:
                right = mid - 1

        return right
