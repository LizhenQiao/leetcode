"""
Keys:
- Sliding window.
- Easier way would be just use a dictionary to keep s's characters and compared to dctp.
(cleaner and easier logic, slightly larger resource cosuming though.)
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def checkDct(dct):
            for value in dct.values():
                if value != 0:
                    return False
            return True

        dctp = collections.Counter(p)
        counter = len(dctp)
        result = []
        left = right = 0

        while right < len(s):
            if s[right] not in dctp:
                dctp = collections.Counter(p)
                right += 1
                left = right
                continue
            dctp[s[right]] -= 1
            if right - left + 1 < len(p):
                right += 1
                continue
            if checkDct(dctp):
                result.append(left)
            dctp[s[left]] += 1
            right += 1
            left += 1

        return result
