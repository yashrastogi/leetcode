class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count01(s):
            ret = [0, 0]
            for c in s: ret[int(c)] += 1
            return ret
        
        @cache
        def rec(i, zeroes, ones):
            if i == len(strs):
                return 0
            count = count01(strs[i])
            taken = -1
            if count[0] <= zeroes and count[1] <= ones:
                taken = 1 + rec(i+1, zeroes - count[0], ones - count[1])
            not_taken = rec(i+1, zeroes, ones)
            return max(taken, not_taken)
        
        return rec(0, m, n)