"""
Keys:
- Use dictionary instead of array. The idea is that only record indexes which have values. In this way we could greatly reduce
  space consuming.
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.dct = {}
        self.snapshots = []

    def set(self, index: int, val: int) -> None:
        self.dct[index] = val

    def snap(self) -> int:
        self.snapshots.append(self.dct.copy())
        return len(self.snapshots) - 1

    def get(self, index: int, snap_id: int) -> int:
        try:
            return self.snapshots[snap_id][index]
        except:
            return 0
