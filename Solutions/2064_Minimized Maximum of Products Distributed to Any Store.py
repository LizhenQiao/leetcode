"""
Keys:
- Binary Search.
"""


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        def getStoreNum(num):
            storeNum = 0
            for q in quantities:
                storeNum += math.ceil(q / num)
            return storeNum

        while left <= right:
            mid = left + (right - left) // 2
            num = getStoreNum(mid)
            if num <= n:
                right = mid - 1
            else:
                left = mid + 1

        return left
