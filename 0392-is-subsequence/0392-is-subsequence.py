class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        sPtr = 0
        for i, c in enumerate(t):
            if c == s[sPtr]:
                sPtr += 1
            if sPtr == len(s):
                return True
        return False