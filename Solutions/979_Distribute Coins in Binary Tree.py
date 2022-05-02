"""
Keys:
- Not easy to come up with the solution at the first time.
- We choose to traverse from bottom to up. Cause for the bottom there is only one direction(move up), which is very important
  for our recursion. Thus, we perform a post-order form dfs.


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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.moves += abs(root.val + left + right - 1)
            return root.val + left + right - 1

        dfs(root)
        return self.moves
