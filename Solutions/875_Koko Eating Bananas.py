"""
Keys:
- Binary Search.
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getEatingHours(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours

        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            hours = getEatingHours(mid)
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left
