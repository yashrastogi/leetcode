class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float('inf')
        sumCurr = 0
        
        for i in range(len(nums)):
            sumCurr += nums[i]
            maxSum = max(maxSum, sumCurr)
            if sumCurr < 0:
                sumCurr = 0
        return maxSum