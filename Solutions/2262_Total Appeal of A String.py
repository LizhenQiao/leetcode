"""
Keys:
- All Substring problem.
"""


class Solution:
    def appealSum(self, s: str) -> int:
        result = 0
        dct = collections.defaultdict(list)
        for i, c in enumerate(s):
            dct[c].append(i)

        result = len(dct) * len(s) * (len(s) + 1) // 2

        for lst in dct.values():
            lst0 = [-1] + lst + [len(s)]
            for i in range(1, len(lst0)):
                result -= (lst0[i] - lst0[i-1]) * \
                    (lst0[i] - lst0[i-1] - 1) // 2

        return result
