"""
Keys:
- Need to get familiar with iteration methods for Tree-traverse problems.

Complexity:
Time: O(n)
Space: O(n)
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Preorder:
# Recursive:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def preorder(root):
            if not root:
                return None
            lst.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return lst

# Iterative:


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root

        while stack or cur:
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.right:
                cur = node.right

        return result


# Inorder:
# Recursive:
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result


# Iterative:
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            result.append(node.val)
            if node.right:
                cur = node.right

        return result


# Postorder:
# Recursive:
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postorder(root):
            if not root:
                return None
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)

        postorder(root)
        return result

# Iterative:


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        cur = root

        while stack or cur:
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.right
            node = stack.pop()
            if node.left:
                cur = node.left

        return result[::-1]
