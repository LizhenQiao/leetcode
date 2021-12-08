"""
Keys:
- BFS
- Layer instead of queue because we need to distinguish each layer for this question.
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        layer = collections.defaultdict(list)
        layer[beginWord].append([beginWord])

        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer.keys():
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            for path in layer[word]:
                                newLayer[newWord].append(path + [newWord])
            wordSet -= newLayer.keys()
            layer = newLayer

        return []
