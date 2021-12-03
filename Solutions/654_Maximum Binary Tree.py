"""
Complexity:
O(n^2)
"""


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxnum = max(nums)
        maxnumindex = nums.index(maxnum)
        root = TreeNode(maxnum)
        root.left = self.constructMaximumBinaryTree(nums[:maxnumindex])
        root.right = self.constructMaximumBinaryTree(nums[maxnumindex+1:])
        return root
