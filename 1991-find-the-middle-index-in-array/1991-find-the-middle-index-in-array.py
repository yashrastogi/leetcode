class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        i = 0
        while i < len(nums):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            i += 1
        return -1
