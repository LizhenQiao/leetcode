"""
Keys:
- A more complex format of 208.(fundamental prefix tree)
- Deal with "*": Add a function with params (word, cur) intead of always start from root in the simplest case. 
- Use self.result(Boolean) intead of return True/False
"""


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.wordEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.wordEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        self.result = False
        self.helper(word, cur)
        return self.result

    def helper(self, word, cur):
        if not word:
            if cur.wordEnd:
                self.result = True
            return None
        c = word[0]
        if c != ".":
            if c not in cur.children:
                return None
            self.helper(word[1:], cur.children[c])
        else:
            for node in cur.children.values():
                self.helper(word[1:], node)
