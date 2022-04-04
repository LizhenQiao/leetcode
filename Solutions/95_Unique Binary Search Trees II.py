"""
Keys:
- This is a recursion problem.
- The solution provided doesn't contain duplicate compression.
- I personally think this question pretty tricky and a little hard to come up with in the first case, especially noticing that the solution have such bad time complexity and space complexity.
- One thing worth noticing is that we need to create whole tree root nodes for every possibility of tree. 

"""


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)

                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)

                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generate_trees(1, n) if n else []
