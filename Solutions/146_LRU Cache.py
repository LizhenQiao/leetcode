# Keys:
# OrderedDict
# - move_to_end()
# - popitem()

# Complexity:
# Time: O(1)

# Code:
import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.dct = collections.OrderedDict()
        self.freespace = capacity

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        self.dct.move_to_end(key)
        return self.dct[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.dct.move_to_end(key)
        else:
            if self.freespace == 0:
                self.dct.popitem(last=False)
            else:
                self.freespace -= 1

        self.dct[key] = value
