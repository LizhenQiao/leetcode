"""
Just to know how to define customed sort in Python.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sortRule(log):
            label, content = log.split(" ", 1)
            if content[0].isdigit():
                return (1, )
            else:
                return (0, content, label)

        return sorted(logs, key=sortRule)
