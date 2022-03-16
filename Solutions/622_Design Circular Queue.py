"""
Keys:
- Inplementation of Circular.

def __init__(self, k: int):
    self.size = k
    self.queue = [0] * k
    self.headIndex = 0
    self.filledSize = 0

"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k
        self.headIndex = 0
        self.filledSize = 0

    def enQueue(self, value: int) -> bool:
        if self.filledSize == self.size:
            return False
        self.queue[(self.headIndex + self.filledSize) % self.size] = value
        self.filledSize += 1
        return True

    def deQueue(self) -> bool:
        if not self.filledSize:
            return False
        self.headIndex = (self.headIndex + 1) % self.size
        self.filledSize -= 1
        return True

    def Front(self) -> int:
        if not self.filledSize:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        if not self.filledSize:
            return -1
        return self.queue[(self.headIndex + self.filledSize - 1) % self.size]

    def isEmpty(self) -> bool:
        return not self.filledSize

    def isFull(self) -> bool:
        return self.filledSize == self.size
