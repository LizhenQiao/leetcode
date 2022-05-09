"""
Keys:
- Binary Search.
"""


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def getSubPilesNum(num):
            subPilesNum = 0
            for c in candies:
                subPilesNum += c // num
            return subPilesNum

        if sum(candies) < k:
            return 0

        left = 1
        right = max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            pilesNum = getSubPilesNum(mid)
            if pilesNum >= k:
                left = mid + 1
            else:
                right = mid - 1

        return right
