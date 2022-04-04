"""
Keys:
- I haven't already accomplished this question by myself, so I won't leave specific code here.

- Method 1: Path Search.
  - First construct graph by the input equations. For example, a/b = 2.0, we add two edge. a -> b with weight 2.0; b -> a with
    weight 0.5. (According to my personal habit, I will probably construct the graph using `collections.defaultdict(list / set)`)
  - Then perform DFS + Backtracking to traverse every possible paths to find a path from source to target and calculate the
    weight product through this process.
  - Handle corner case such as node not in the graph. But above are the main steps.

  Complexity:
  Time: O(m*n)
  Space: O(n)

- Method 2: Union-Find with Weights.

  - Haven't interpret it. Union-Find for weighted graph.

"""

# To see more details: https://leetcode.com/problems/evaluate-division/solution/
