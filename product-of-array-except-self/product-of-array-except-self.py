class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(nums)
        leftProducts = [1] * len(nums)
        rightProducts = [1] * len(nums)
        for i in range(len(nums)-1):
            leftProducts[i+1] = nums[i] * leftProducts[i]
        for j in reversed(range(1, len(nums))):
            rightProducts[j-1] = nums[j] * rightProducts[j]
        
        ret = []
        for i in range(len(nums)):
            ret.append(leftProducts[i] * rightProducts[i])
        return ret
        