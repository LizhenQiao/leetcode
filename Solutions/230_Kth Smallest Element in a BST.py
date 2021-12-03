"""
Keys:
Fundamental inorder traversal

Complexity:
Time: O(n)
Space: O(1)
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = k-1
        self.result = None

        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            if self.counter == 0:
                self.result = root.val
            self.counter -= 1
            inorder(root.right)

        inorder(root)
        return self.result
