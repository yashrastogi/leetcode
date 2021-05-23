class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                ret.append(nums[i])
        return ret