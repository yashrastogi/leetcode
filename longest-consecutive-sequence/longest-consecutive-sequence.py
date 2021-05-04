def consec_len(i, nums):
    lenx = 1
    for j in range(i, len(nums)-1):
        if nums[j]+1 == nums[j+1]:
            lenx += 1
        else:
            break
    return lenx

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = [x for x in set(nums)]
        nums.sort()
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        print(nums)
        max_len = 0
        for i in range(len(nums)-1):
            max_len = max(max_len, consec_len(i, nums))
        return max_len