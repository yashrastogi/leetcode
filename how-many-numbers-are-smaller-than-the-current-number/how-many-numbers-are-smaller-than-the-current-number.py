class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = []
        for i, num in enumerate(nums):
            count_smaller = 0
            for j in range(0, len(nums)):
                if num > nums[j] and i != j:
                    count_smaller += 1
            ret.append(count_smaller)
        return ret