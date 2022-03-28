"""
Keys:
DFS with "None" value

Complexity:
Time: O(n)

Code:

"""


class Codec:

    def serialize(self, root):
        self.resultstr = ""

        def helper(root):
            if not root:
                self.resultstr += "None" + "*"
                return None
            self.resultstr += str(root.val) + "*"
            helper(root.left)
            helper(root.right)

        helper(root)
        return self.resultstr

    def deserialize(self, data):
        lst = data.split("*")[:-1]

        def buildTree():
            rootval = lst.pop(0)
            if rootval == "None":
                return None
            root = TreeNode(rootval)
            root.left = buildTree()
            root.right = buildTree()
            return root

        return buildTree()
