"""
Keys:
- Sliding window.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        dct = collections.defaultdict(int)
        maxl = 0
        left = 0

        for right in range(len(s)):
            while s[right] not in dct and len(dct) == k:
                dct[s[left]] -= 1
                if dct[s[left]] == 0:
                    del dct[s[left]]
                left += 1
            dct[s[right]] += 1
            maxl = max(maxl, right - left + 1)

        return maxl
