"""
Keys:
- Stack and Hashtable.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = collections.defaultdict(int)
        stack = []

        for log in logs:
            logid, action, timestamp = log.split(":")
            if action == "end":
                _, popTimestamp = stack.pop()
                period = int(timestamp) - int(popTimestamp) + 1
                result[int(logid)] += period
                if stack:
                    result[int(stack[-1][0])] -= period
            else:
                stack.append((logid, timestamp))

        return [result[logid] for logid in sorted(result.keys())]
