"""
Keys:
- All Substring problem.
"""


class Solution:
    def countVowels(self, word: str) -> int:
        result = 0
        for i, c in enumerate(word):
            if c in "aeiou":
                result += (i+1) * (len(word)-i)

        return result
