"""
Keys:
- Using the property of BST. While I personally find it uneasy to come up with this concise solution.

Complexity:
Time: O(n)
"""


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        suc = None
        self.target = p.val

        while root:
            if root.val <= self.target:
                root = root.right
            else:
                suc = root
                root = root.left

        return suc
