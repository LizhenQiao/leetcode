"""
Keys:
Preprocessing of input by using function of Python.

Complexity:
Time: O(n)
"""


class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        counter = collections.Counter(
            word for word in paragraph.lower().strip().split())

        targetWord, maxnum = None, 0

        for word, num in counter.items():
            if num > maxnum and word not in banset:
                maxnum = num
                targetWord = word

        return targetWord
