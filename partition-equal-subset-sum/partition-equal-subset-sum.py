class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        subset_sum = sum_nums / 2
        @cache
        def recurse(n, sums):
            if n == len(nums):
                return False
            if sums > subset_sum:
                return False
            if sums == 0:
                return True
            return recurse(n+1, sums) or recurse(n+1, sums-nums[n])
        
        return recurse(0, subset_sum)
            
            
        
        