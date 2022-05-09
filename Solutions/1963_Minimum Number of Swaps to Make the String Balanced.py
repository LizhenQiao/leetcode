"""
Keys:
- Greedy thinking.

Complexity:
Time: O(n)
Space: O(1)
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        counter = 0
        swap = 0

        for c in s:
            if c == "[":
                counter += 1
            else:
                if counter:
                    counter -= 1
                else:
                    counter += 1
                    swap += 1

        return swap
