# Prefix Sum related questions

---

- [523 | Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

  - [solution](../../Solutions/523_Continuous%20Subarray%20Sum.py)

- [560 | Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

  - [solution](../../Solutions/560_Subarray%20Sum%20Equals%20K.py)

- [974 | Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

  - [solution](../../Solutions/974_Subarray%20Sums%20Divisible%20by%20K.py)

- [1658 | Minimum Operations to Reduce X to Zero \*\*\*](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

  - [solution](../../Solutions/1658_Minimum%20Operations%20to%20Reduce%20X%20to%20Zero.py)

- [304 | Range Sum Query 2D - Immutable \*\*](https://leetcode.com/problems/range-sum-query-2d-immutable/)

  - [solution](../../Solutions/304_Range%20Sum%20Query%202D%20-%20Immutable.py)

---

## Summary

Usually we try to solve a problem using `Prefix Sum` when the question ask something related to "Sum of subarray". The logic here is that we could easily get any subarray's sum by calculating `Prefix Sum` in advance. Furthermore, combined with a hash table, we could make some check process in O(1) time. This is typically why and when we perform a `prefix sum` in an algorithm, it is a one-pass O(n) time complexity.

Examples above are some of the classic questions using prefix sum.

The complete solution often combined the Prefix Sum with Hash Table. (Not necessary)
