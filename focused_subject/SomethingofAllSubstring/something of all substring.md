# All Substring related questions

---

- [828 | Count Unique Characters of All Substrings of a Given String](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)

  - [solution](../../Solutions/828_Count%20Unique%20Characters%20of%20All%20Substrings%20of%20a%20Given%20String.py)

- [907 | Sum of Subarray Minimums \*](https://leetcode.com/problems/sum-of-subarray-minimums/)

  - [solution](../../Solutions/907_Sum%20of%20Subarray%20Minimums.py)

- [2104 | Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)

  - [solution](../../Solutions/2104_Sum%20of%20Subarray%20Ranges.py)

- [2262 | Total Appeal of A String](https://leetcode.com/problems/total-appeal-of-a-string/)

  - [solution](../../Solutions/2262_Total%20Appeal%20of%20A%20String.py)

- [2063 | Vowels of All Substrings](https://leetcode.com/problems/vowels-of-all-substrings/)

  - [solution](../../Solutions/2063_Vowels%20of%20All%20Substrings.py)

---

## Summary

This kind of questions ask for something of all substrings or subarrays.

- Basically we don't really traverse all possible cases and check each case one by one. Instead, we calculate each character in string / num in array's #cases and sum them up.
  - For strings, we usually use dictionary to get each character's indexes as first step(Not necessary)
  - For arrays, we tend to use something like monotonic stack.

We could somehow transfer/simplify the question by utilizing features of the string and XX (What we are supposed to count)
Take this question as an example:
We transfer "Count Unique Characters of All Substrings of a Given String" into "Count each character's number of cases to be
Unique in a string and sum them up."
