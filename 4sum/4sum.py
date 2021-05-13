class Solution:
    def fourSum(self, nums: List[int], target) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, start=0, k=4, target=target)
    
    def twoSum(self, nums: List[int], start, target: int) -> List[List[int]]:
        res = []
        lo, hi = start, len(nums) - 1
        while (lo < hi):
            sum = nums[lo] + nums[hi]
            if sum < target or (lo > start and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return res
    
    def kSum(self, nums, start, k, target):
        if start > len(nums) - k + 1:
            return
        if nums[start] * k > target or nums[-1] * k < target:
            return
        if k == 2:
            return self.twoSum(nums, start, target)
        
        ret = []
        i = start
        while i < len(nums):
            while i+1 < len(nums) and i > start and nums[i] == nums[i-1]:
                i += 1
            curr = self.kSum(nums, i+1, k-1, target - nums[i])
            if curr:
                for pair in curr:
                    ret.append([nums[i]] + pair)
            i += 1
        return ret