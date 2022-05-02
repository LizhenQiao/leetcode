"""
Keys:
- A pretty obvious DP.
- A point worth mention is that sometimes use `Dictionary(Hash Table)` for status of DP is the better choice. For me, 
  sometimes I tend to think of using array for dp at the first time.
- One thing to notice is that we need to take string manipulation into consideration while considering time complexity.
  I frequently forget it.

Complexity:
time: O(n * (logn + len(n)^2))
space: O(n)
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: len(word))
        dp = {}
        for word in words:
            dp[word] = 1

        for word in words:
            for i in range(len(word)):
                newWord = word[:i] + word[i+1:]
                if newWord in dp:
                    dp[word] = max(dp[word], dp[newWord] + 1)

        return max(dp.values())
