class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_len = 1
        set_nums = set(nums)
        i = 0
        for num in nums:
            if num - 1 not in set_nums:
                last_num = num
                curr_len = 1
                while last_num + 1 in set_nums:
                    curr_len += 1
                    last_num += 1
                max_len = max(max_len, curr_len)
        return max_len