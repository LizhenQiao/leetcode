"""
Keys:
- Prefix of words, obviously a prefix tree question.
- Foundations of Prefix Tree should be very familiar.

Complexity:
n refers to length of sentence.
Time: O(n)
Space: O(n)
"""


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = ""

    def addWord(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.word = word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []
        root = TrieNode()

        for word in dictionary:
            root.addWord(word)

        for word in sentence.split(" "):
            cur = root
            for i, c in enumerate(word):
                if c not in cur.children or i == len(word) - 1:
                    result.append(word)
                    break
                else:
                    cur = cur.children[c]
                    if cur.word:
                        result.append(cur.word)
                        break
        return " ".join(result)
