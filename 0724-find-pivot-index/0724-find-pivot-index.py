class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums) - nums[0]
        i = 0
        while i < len(nums):
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            i += 1
            if i < len(nums):
                rightSum -= nums[i]
            else:
                rightSum = 0
        return -1
