class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        charMap = defaultdict(list)
        for i, c in enumerate(t):
            charMap[c] += [i]
        print(charMap)
        for i, c in enumerate(s):
            pass
        return False
