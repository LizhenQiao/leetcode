"""
Keys:
- To represent structure of a tree(node), both preorder and postorder make sense, while inorder not.
- We could also use a defaultdict(list) to replace two sets, this could make code simpler.

Complexity:
Time: O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        haveReported = set()
        subtreeSet = set()

        def postorder(root):
            if not root:
                return ["None"]
            leftPath = postorder(root.left)
            rightPath = postorder(root.right)
            path = leftPath + rightPath + [root.val]
            pathTuple = tuple(path)
            if pathTuple in subtreeSet and pathTuple not in haveReported:
                haveReported.add(pathTuple)
                result.append(root)
            else:
                subtreeSet.add(pathTuple)
            return path

        postorder(root)
        return result
