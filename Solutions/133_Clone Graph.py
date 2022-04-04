"""
Keys:
- Deep copy of both Graph and Linked List use the dictionary / hashtable data structure.
- DFS to accomplish this question.

Complexity:
Time: O(V + E)
Space: O(V + E)

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        self.dct = {}

        def cloneNode(node):
            if node in self.dct:
                return self.dct[node]
            newNode = Node(node.val, [])
            self.dct[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(cloneNode(neighbor))
            return self.dct[node]

        return cloneNode(node)
