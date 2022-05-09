"""
Keys:
- A useful trick (when doing any parentheses validation) is to greedily check balance left-to-right, and then right-to-left.
  - Left-to-right check ensures that we do not have orphan ')' parentheses.
  - Right-to-left checks for orphan '(' parentheses.

- For questions asking whether a Parentheses String could be valid (Some of the characters in the string could be either "(" or 
  ")".), they all share this solving idea. Let's just call it `Positive and Negative Traverse`. 

Complexity:
Time: O(n)
Space: O(1)
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        # Check in the positive order to see if the string has too many ")" so that the string would not be valid. (Not closed)
        counter1 = 0
        for i in range(len(s)):
            if locked[i] == "1":
                if s[i] == "(":
                    counter1 += 1
                else:
                    counter1 -= 1
            else:
                counter1 += 1
            if counter1 < 0:
                return False

        # Check in the reverse order to see if the string has too many "("
        counter2 = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == "1":
                if s[i] == "(":
                    counter2 -= 1
                else:
                    counter2 += 1
            else:
                counter2 += 1
            if counter2 < 0:
                return False

        return True
