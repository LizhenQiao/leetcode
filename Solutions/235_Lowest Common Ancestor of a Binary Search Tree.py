"""
Keys:
- LCA of BST, we could use the property of BST, traverse from the above, the first node whose value sits between p.val and
  q.val is the lca.

Complexity:
Time: O(logn)
Space: O(1)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        pval, qval = p.val, q.val
        bigval = max(pval, qval)
        smallval = min(pval, qval)
        cur = root
        while cur:
            if cur.val <= bigval and cur.val >= smallval:
                return cur
            else:
                if cur.val > bigval:
                    cur = cur.left
                else:
                    cur = cur.right
