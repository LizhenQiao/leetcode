```
Keys:
self.maxf = 0
self.counter = collections.defaultdict(int)
self.layer = collections.defaultdict(list)

Complexity:
Time: O(1)

Code:
class FreqStack:

    def __init__(self):
        self.maxf = 0
        self.counter = collections.defaultdict(int)
        self.layer = collections.defaultdict(list)

    def push(self, val: int) -> None:
        f = self.counter[val] + 1
        self.counter[val] = f
        if f > self.maxf:
            self.maxf = f
        self.layer[f].append(val)

    def pop(self) -> int:
        popnum = self.layer[self.maxf].pop()
        self.counter[popnum] -= 1
        if not self.layer[self.maxf]:
            self.maxf -= 1
            del self.layer[self.maxf + 1]
        return popnum

```
