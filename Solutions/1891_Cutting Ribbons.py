"""
Keys:
- Binary Search.

Complexity:
Time: O(n*logn)
Space: O(1)
"""


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, max(ribbons)

        while left <= right:
            mid = left + (right - left) // 2
            res = 0
            for ribbon in ribbons:
                res += ribbon // mid
            if res >= k:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1
