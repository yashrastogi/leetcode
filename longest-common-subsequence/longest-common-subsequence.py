class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1) + 1, len(s2) + 1
        dp = [[-1] * l2 for _ in range(l1)]
        
        @lru_cache(maxsize=None)
        def rec(l1x, l2x):
            if l1x == 0 or l2x == 0:
                return 0
            if s1[l1x - 1] == s2[l2x - 1]:
                ret = 1 + rec(l1x - 1, l2x - 1)
            else:
                ret = max(rec(l1x, l2x - 1), rec(l1x - 1, l2x))
            return ret
        
        return rec(len(s1), len(s2))