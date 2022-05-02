"""
Keys:
- "Sum of Subarray Minimums" => "Count each number's #cases to be the minimum one of a certain subarray"
- Utilize `Monotonic Stack` to get each numbers pre-larger number and post-larger number.
- One tip of `Monotonic Stack`: Insert two values to start and end of array to ensure that are values would be popped
  during our iteration.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr = [-float('inf')] + arr + [-float('inf')]
        result = 0

        for index, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                popIndex = stack.pop()
                result += (popIndex - stack[-1]) * \
                    (index - popIndex) * arr[popIndex]
            stack.append(index)

        return result % (10 ** 9 + 7)
