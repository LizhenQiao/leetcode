"""
Keys:
- Sliding window.
- Asking for `longest substring` of a string, obviously could be solved by sliding window.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dct = collections.defaultdict(int)
        left = 0
        maxl = 0

        for right in range(len(s)):
            while s[right] not in dct and len(dct) == 2:
                dct[s[left]] -= 1
                if dct[s[left]] == 0:
                    del dct[s[left]]
                left += 1
            dct[s[right]] += 1
            maxl = max(maxl, right - left + 1)

        return maxl
