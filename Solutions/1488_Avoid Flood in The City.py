# Keys:
# - Keep dry days in the list
#   use the dryday to dry the lake until we get a rain on the lake which was already rained before.

# Complexity:
# Time: O(n^2)

# Code:
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        fullLakes = {}
        dryDays = []
        result = [1] * n

        for i in range(n):
            if rains[i] == 0:
                dryDays.append(i)
            else:
                result[i] = -1
                if rains[i] not in fullLakes:
                    fullLakes[rains[i]] = i
                else:
                    if not dryDays:
                        return []
                    for j in range(len(dryDays)):
                        if dryDays[j] > fullLakes[rains[i]]:
                            result[dryDays[j]] = rains[i]
                            dryDays.pop(j)
                            fullLakes[rains[i]] = i
                            break
                        if j == len(dryDays) - 1 and dryDays[j] <= fullLakes[rains[i]]:
                            return []
        return result
