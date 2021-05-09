class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        def m(i,j):
            return i - j if i > j else j - i
        
        count = 0
        di = {c: i for i, c in enumerate(keyboard)}
        curr = 0
        for c in word:
            count += m(curr, di[c])
            curr = di[c]
        return count