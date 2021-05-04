from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def rec(idx, jumpsize):
            for i in range(idx+1, len(stones)):
                gap = stones[i] - stones[idx]
                if gap <= jumpsize+1 and gap >= jumpsize-1:
                    if rec(i, gap):
                        return True
            if idx == len(stones)-1:
                return True
            return False
            
        return rec(0, 0)