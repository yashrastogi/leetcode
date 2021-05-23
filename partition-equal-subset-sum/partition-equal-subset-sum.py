class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        tSum = int(totalSum/2)
        ret = False
        
        @cache
        def rec(idx, sums):
            nonlocal ret, tSum
            if ret: return
            if idx == len(nums): return
            if sums == tSum: ret = True
            rec(idx+1, sums + nums[idx])
            rec(idx+1, sums)
        
        rec(0, 0)
        return ret