class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_len = 1
        set_nums = set(nums)
        i = 0
        while i < len(nums):
            if nums[i] - 1 not in set_nums:
                last_num = nums[i]
                curr_len = 1
                while last_num + 1 in set_nums:
                    curr_len += 1
                    max_len = max(max_len, curr_len)
                    last_num += 1
            i += 1
        return max_len