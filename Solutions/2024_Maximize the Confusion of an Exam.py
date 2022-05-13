"""
Keys:
- Sliding Window.
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        countert = counterf = 0
        left = 0
        maxl = 0

        for right in range(len(answerKey)):
            if answerKey[right] == "T":
                countert += 1
            else:
                counterf += 1
            if min(countert, counterf) > k:
                if answerKey[left] == "T":
                    countert -= 1
                else:
                    counterf -= 1
                left += 1

        return len(answerKey) - left
