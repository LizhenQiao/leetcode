"""
Keys:
- Idea is to find first number which is not the biggest among rest numbers left at right side. Then exchange it with the 
  rightmost biggest number.

Complexity:
Time: O(n^2)
Space: O(n)
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        if not num or num < 10:
            return num

        index = 0
        strnum = list(str(num))
        while strnum and strnum[0] == max(strnum):
            index += 1
            strnum = strnum[1:]
        if not strnum:
            return num
        strmaxnum = max(strnum)
        for i in range(len(strnum)-1, -1, -1):
            if strnum[i] == strmaxnum:
                maxIndex = i
                break
        strnum[0], strnum[maxIndex] = strnum[maxIndex], strnum[0]

        return int(str(num)[:index] + "".join(strnum))
