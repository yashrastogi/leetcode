class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        di = {el: i for i,el in enumerate(order)}
        s = sorted(words, key=lambda word: [di[c] for c in word])
        return words == s