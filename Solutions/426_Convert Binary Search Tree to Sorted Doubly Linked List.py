"""
Keys:
- Just a normal inorder tranverse with storage of preNode. Commonly seen in leetcode.


Complexity:
time: O(V)
space: O(1)
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        self.preNode = Node(0)

        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            self.preNode.right = root
            root.left = self.preNode
            self.preNode = root
            inorder(root.right)

        inorder(root)

        cur = root
        while cur and cur.left and cur.left.left:
            cur = cur.left
        firstNode = cur

        cur = root
        while cur and cur.right:
            cur = cur.right
        lastNode = cur

        firstNode.left = lastNode
        lastNode.right = firstNode

        return firstNode
