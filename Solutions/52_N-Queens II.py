"""
Keys:
- This is a recursion problem with backtracking.
- A useful knowledge for this question would be how to represent each diagonal or anti-diagonal: `row + column` and `row - column`
- The rest parts are just normal recursion problems(row number as the recursion sign), by using three sets to check. `column`, 'diagonal', 'anti-diagonal'. 

Complexity:
Time: O(n!)
Space: O(n)
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(row: int) -> int:
            if row == n:
                self.counter += 1
                return None
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    helper(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        self.counter = 0
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        helper(0)
        return self.counter
