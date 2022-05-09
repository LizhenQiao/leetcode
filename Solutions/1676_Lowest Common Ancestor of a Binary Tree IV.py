"""
Keys:
- A more common version of Classic LCA (Leetcode236), the basic idea is still the same. Just some changes in details. 

Complexity:
Time: O(n)
Space: O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.lca = None

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            mid = root in nodes
            if mid + left + right == len(nodes):
                self.lca = root
                return -1
            return mid + left + right

        dfs(root)
        return self.lca
