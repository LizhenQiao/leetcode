"""
Keys:
- Binary Search.

Complexity:
Time: O(n * logx)
Space: O(1)
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        summ = sum(weights)
        left = max(summ // days, max(weights))
        right = summ

        def getDaysNeed(capacity):
            c = capacity
            daysNeed = 1
            for w in weights:
                if w > c:
                    c = capacity - w
                    daysNeed += 1
                else:
                    c -= w
            return daysNeed

        while left <= right:
            mid = left + (right - left) // 2
            daysNeed = getDaysNeed(mid)
            if daysNeed <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left
