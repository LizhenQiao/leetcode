"""
Keys:
- A typical problem for using QuickSelect.
- Need to practice more questions related to QuickSelect!


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [num for num in nums if num < pivot]
        right = [num for num in nums if num > pivot]
        mid = [num for num in nums if num == pivot]
        ll, lr, lm = len(left), len(right), len(mid)

        if lr >= k:
            return self.findKthLargest(right, k)
        elif lr + lm < k:
            return self.findKthLargest(left, k - lr - lm)
        else:
            return pivot
