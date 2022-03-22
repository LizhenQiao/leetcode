"""
Keys:
- Inspiration: to accomplish O(1) delete of list. We could use a hash table to store the index of each number in
  the list, perform `lst[index], lst[i] = lst[i], lst[index]`, then pop the last number.
  O(n) space for O(1) time. it's really a tradeoff.  
"""


from random import choice


class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dct = {}

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        self.dct[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False
        index = self.dct[val]
        self.lst[index], self.lst[-1] = self.lst[-1], self.lst[index]
        self.dct[self.lst[index]] = index
        del self.dct[self.lst[-1]]
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.lst)
