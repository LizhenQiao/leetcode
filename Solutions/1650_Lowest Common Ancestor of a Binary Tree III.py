"""
Keys:
- One of the typical idea of solving LCA problem. Find the first common node of `pToRoot Path` and `qToRoot Path`.

Complexity:
Time: O(n)
Space: O(n)
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pParent = set()
        while p:
            pParent.add(p)
            p = p.parent

        while q:
            if q in pParent:
                return q
            q = q.parent
