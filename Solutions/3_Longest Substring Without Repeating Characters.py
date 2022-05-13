"""
Keys:
- Sliding window.
- Asking for `longest substring` of a string, obviously could be solved by sliding window.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        cSet = set()
        left = 0

        for right in range(len(s)):
            while s[right] in cSet:
                cSet.remove(s[left])
                left += 1
            cSet.add(s[right])
            maxl = max(maxl, right - left + 1)

        return maxl
