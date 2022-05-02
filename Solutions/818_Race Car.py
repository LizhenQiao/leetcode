"""
Keys:
- Could be solved by BFS. It is reasonable to think of using BFS (sometimes I could, sometimes I cannot). It might not be that
  obvious as most of the questions.

Complexity:
Space: O(n)
"""


class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque()
        queue.append((0, 0, 1))
        visited = set()
        visited.add((0, 1))

        while queue:
            l, pos, speed = queue.popleft()
            if pos == target:
                return l
            if (pos + speed, speed * 2) not in visited:
                queue.append((l+1, pos + speed, speed * 2))
                visited.add((pos + speed, speed * 2))
            if pos + speed > target and speed > 0 and (pos, -1) not in visited:
                queue.append((l+1, pos, -1))
                visited.add((pos, -1))
            elif pos + speed < target and speed < 0 and (pos, 1) not in visited:
                queue.append((l+1, pos, 1))
                visited.add((pos, 1))
