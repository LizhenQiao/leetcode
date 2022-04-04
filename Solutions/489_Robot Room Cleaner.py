"""
Keys:
- This is a recursion problem with backtracking. Cause if we want to traverse every possible cells in the puzzle, we need to check and perform all four directions of each cells.
- To hold a hashtable to record the cells we have already seen, we establish a coordinate system which represent first position as (0, 0).
- The result part is a typical dfs recursion and backtracking process.

Complexity:
N is the number of empty cells.
Time: O(N)
Space: O(N)

"""


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set())

    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))

        for k in range(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y,
                         direction_x, direction_y, visited)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x
