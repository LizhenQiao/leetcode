"""
Keys:
- A classic question of Binary Tree.
- While analyzing space complexity of recursion, we need to take call stack of function into consideration. 

Complexity:
Time: O(n)
Space: O(n)

This is because the maximum amount of space utilized by the recursion stack would be NN since the height of
a skewed binary tree could be N.
While analyzing space complexity of recursion, we need to take call stack of function into consideration. 
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return False
        self.resultNode = None

        def helper(root, p, q):
            if not root:
                return False
            left = helper(root.left, p, q)
            mid = root == p or root == q
            right = helper(root.right, p, q)
            if left + mid + right > 1:
                self.resultNode = root
            return left or mid or right

        helper(root, p, q)
        return self.resultNode
