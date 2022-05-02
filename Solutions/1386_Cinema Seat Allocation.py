"""
Keys:
- It's more about finding regularity or math.
- Some implementation details are clever.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dct = collections.defaultdict(set)

        for row, column in reservedSeats:
            if column in (2, 3, 4, 5):
                dct[row].add(1)
            if column in (4, 5, 6, 7):
                dct[row].add(2)
            if column in (6, 7, 8, 9):
                dct[row].add(3)

        result = 2 * n
        for lst in dct.values():
            if len(lst) == 3:
                result -= 2
            else:
                result -= 1

        return result
