class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1]
        for i in range(1, len(nums)):
            ret.append(ret[i - 1] * nums[i - 1])
        temp_prefix = 1
        for j in reversed(range(len(nums))):
            ret[j] = ret[j] * temp_prefix
            temp_prefix *= nums[j]
        return ret