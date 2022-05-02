"""
Keys:
- A little bit tricky one. Pretty interesting solution.

Complexity:
time: O(10*n)
space: O(n)
"""


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        def findMatch(lst, w, k):
            filterList = []
            for word in lst:
                counter = 0
                for c1, c2 in zip(w, word):
                    if c1 == c2:
                        counter += 1
                if counter == k:
                    filterList.append(word)
            return filterList

        for _ in range(10):
            index = random.randint(0, len(wordlist)-1)
            word = wordlist[index]
            res = master.guess(word)
            if res == 6:
                return word
            wordlist = findMatch(wordlist, word, res)

        return word
