"""
Keys:
- Use pointer, a little bit tricky to me.

Complexity:
Time: O(rows * cols)
Space: O(1)
"""


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        l = len(s)
        cur = 0

        for _ in range(rows):
            cur += cols - 1
            if s[cur % l] == " ":
                cur += 1
            elif s[(cur + 1) % l] == " ":
                cur += 2
            else:
                while cur > 0 and s[cur % l] != " ":
                    cur -= 1
                cur += 1

        return cur // l
