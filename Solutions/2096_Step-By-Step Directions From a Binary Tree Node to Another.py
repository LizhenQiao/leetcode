"""
Keys:
- LCA question.

Complexity:
Time: O(n)
Space: O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = [(root.val, "")]
        result = ""

        def getPathFromRoot(root, target):
            if root.val == target:
                return True
            if root.left:
                path.append((root.left.val, "L"))
                res = getPathFromRoot(root.left, target)
                if res:
                    return True
                path.pop()
            if root.right:
                path.append((root.right.val, "R"))
                res = getPathFromRoot(root.right, target)
                if res:
                    return True
                path.pop()

        getPathFromRoot(root, startValue)
        path1 = path[:]
        path = [(root.val, "")]
        getPathFromRoot(root, destValue)
        path2 = path[:]

        nodeSet = set([node[0] for node in path2])

        firstParentNode = None
        for node in path1[::-1]:
            if node[0] in nodeSet:
                firstParentNode = node[0]
                break
            result += "U"

        index = 0
        for i in range(len(path2)):
            if path2[i][0] == firstParentNode:
                index = i
                break
        for node in path2[index+1:]:
            result += node[1]

        return result
