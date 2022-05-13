"""
Keys:
- Sliding Window.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct = collections.defaultdict(int)
        left = 0
        maxl = 0

        for right in range(len(s)):
            dct[s[right]] += 1
            while right - left + 1 - max(dct.values()) > k:
                dct[s[left]] -= 1
                left += 1
            maxl = max(maxl, right - left + 1)

        return maxl


# Potential optimization.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        left = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            maxf = max(counter.values())
            if right - left + 1 - maxf > k:
                counter[s[left]] -= 1
                left += 1

        return len(s) - left
