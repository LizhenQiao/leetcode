"""
Keys:
- Similar to BFS
- keep leftmost of each layer

Complexity:
Time: O(V)
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        leftmost = root
        while leftmost:
            cur = leftmost
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                cur = cur.next
            leftmost = leftmost.left
        return root
