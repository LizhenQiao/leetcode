"""
Keys:
- Plus version of Serialize and Deserialize Binary Tree. Compare and deeper understand.
- Use a signal ("None" for example) to record end of a layer of N-ary Tree.

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


class Codec:
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ""
        self.resultStr = ""

        def preorder(root):
            self.resultStr += str(root.val) + "*"
            for child in root.children:
                preorder(child)
            self.resultStr += "None" + "*"

        preorder(root)
        return self.resultStr

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        lst = data.split("*")[:-1]

        def buildTree(root):
            while lst[0] != "None":
                popVal = int(lst.pop(0))
                node = Node(popVal, [])
                root.children.append(node)
                buildTree(node)
            lst.pop(0)
            return None

        root = Node(int(lst.pop(0)), [])
        buildTree(root)
        return root
