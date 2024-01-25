class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = 0
        curr_zeroes = 0
        max_ones = 0
        while j < len(nums):
            if curr_zeroes > k:
                if nums[i] == 0:
                    curr_zeroes -= 1
                i += 1
            if nums[j] == 0:
                curr_zeroes += 1
            ones = j - i - curr_zeroes + 1
            max_ones = max(max_ones, min(ones + k, len(nums)))
            j += 1
        return max_ones
