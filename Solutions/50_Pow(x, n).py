"""
Keys:
- Obviously could be solved by recursion.
- Notice that need to handle the situation when n is negative. 

Complexity:
Time: O(logn)
Space: O(logn)

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        originaln = n
        if n < 0:
            n *= -1
        if n == 0:
            return 1.0
        sub = self.myPow(x, n // 2)
        absresult = sub * sub if n % 2 == 0 else sub * sub * x
        return absresult if originaln >= 0 else 1 / absresult
