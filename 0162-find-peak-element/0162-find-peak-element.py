class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1 if nums[1] > nums[0] else 0
        
        for i, num in enumerate(nums):
            if i == 0 and num > nums[i + 1]:
                return i
            elif i == len(nums) - 1 and num > nums[i - 1]:
                return i
            elif num > nums[i - 1] and num > nums[i + 1]:
                return i
        
        return -1
