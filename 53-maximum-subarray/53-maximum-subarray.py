class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_till_now = 0
        max_overall = -float('inf')
        for i, num in enumerate(nums):
            max_till_now += num
            max_overall = max(max_overall, max_till_now)
            if max_till_now < 0:
                max_till_now = 0
        return max_overall
        