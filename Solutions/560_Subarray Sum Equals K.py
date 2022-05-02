"""
Keys:
- `Prefix Sum` is the basic trick for this problem. Quite clever and interesting.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumDct = collections.defaultdict(int)
        tmpsum = 0
        counter = 0
        sumDct[0] = 1

        for num in nums:
            tmpsum += num
            if tmpsum - k in sumDct:
                counter += sumDct[tmpsum - k]
            sumDct[tmpsum] += 1

        return counter
