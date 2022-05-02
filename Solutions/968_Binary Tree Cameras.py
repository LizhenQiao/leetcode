"""
Keys:
- Contain some sort of greedy idea in this solution.
- Traverse from bottom to up => Perform a post-order form dfs.


Complexity:
time: O(n)
space: O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(root):
            if not root:
                return 2
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0 or right == 0:
                self.result += 1
                return 1
            elif left == 1 or right == 1:
                return 2
            else:
                return 0

        return (dfs(root) == 0) + self.result
