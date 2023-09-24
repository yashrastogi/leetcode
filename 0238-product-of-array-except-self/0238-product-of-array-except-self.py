class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = [1]
        ret = []
        for j in reversed(range(len(nums)-1)):
            suffix.append(suffix[-1] * nums[j + 1])
        for i, num in enumerate(nums):
            ret.append(prefix * suffix[-i-1])
            prefix *= nums[i]
        return ret