class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        prefix = [1]
        suffix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i  - 1]* nums[i - 1])
        for j in reversed(range(len(nums)-1)):
            suffix.append(suffix[-1] * nums[j + 1])
        print(prefix, suffix)
        # temp_prefix = 1
        for i, num in enumerate(nums):
            # temp_suffix = 1
            # for j in range(i+1, len(nums)):
                # temp_suffix *= nums[j]
            ret.append(prefix[i] * suffix[-i-1])
            
        return ret