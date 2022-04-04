"""
Keys:
- DFS with Backtracking.
- The time complexity of backtracking is often calculated by considering it as a combination problem.
- One thing to notice: At line 42 - 43. When we want to traverse an array and manipulate it at the same time.
  There might be an issue. Therefore, we need to make a copy of the array, then get element from it. 

Complexity:

Time: O(E^d)
      where E is the number of total flights and d is the maximum number of flights from an airport.
Space: O(V + E)

https://leetcode.com/problems/reconstruct-itinerary/solution/

The complexity analysis worth reading. 


Plus: There is actually simpler solution, but I just go with mine for now.

"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        connections = collections.defaultdict(list)
        path = []
        result = []
        l = len(tickets)

        for location1, location2 in tickets:
            connections[location1].append(location2)

        for connection in connections.values():
            connection.sort()

        def dfs(location, restTickets):
            path.append(location)
            if restTickets == 0:
                result.append(path[:])
                return True
            else:
                if not connections[location]:
                    path.pop()
                    return None
                lst = connections[location][:]
                for nextLocation in lst:
                    connections[location].remove(nextLocation)
                    res = dfs(nextLocation, restTickets - 1)
                    connections[location].append(nextLocation)
                    if res:
                        return True
            path.pop()

        dfs("JFK", l)

        return result[0]
