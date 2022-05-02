"""
Keys:
There might be a common pattern behind questions like "Count XX of all substrings of a given string". Need more practice. 
- The most intuitive brute force solution of questions like this is to perform iterations.
- However, we could somehow transfer/simplify the question by utilizing features of the string and XX (What we are supposed to count)
  Take this question as an example:
  We transfer "Count Unique Characters of All Substrings of a Given String" into "Count each character's number of cases to be
  Unique in a string and sum them up."


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dct = collections.defaultdict(list)
        result = 0

        for index, c in enumerate(s):
            dct[c].append(index)

        for lst in dct.values():
            lst = [-1] + lst + [len(s)]
            for i in range(1, len(lst) - 1):
                result += (lst[i] - lst[i-1]) * (lst[i+1] - lst[i])

        return result % (10**9 + 7)
