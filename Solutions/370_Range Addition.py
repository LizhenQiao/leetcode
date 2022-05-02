"""
Keys:
- The idea for this problem is that for each update operation, we don't need to update all elements between i and j.
  Update only the first and end element is sufficient.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        dp = [0] * length
        for start, end, inc in updates:
            dp[start] += inc
            if end < length-1:
                dp[end+1] -= inc

        for i in range(1, length):
            dp[i] += dp[i-1]

        return dp
