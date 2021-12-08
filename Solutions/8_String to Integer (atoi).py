
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        signal = 1
        num = 0
        if s[0] == "-":
            signal = -1
        if s[0] in ("+", "-"):
            s = s[1:]
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break

        return max(min(num * signal, 2**31 - 1), -2**31)
