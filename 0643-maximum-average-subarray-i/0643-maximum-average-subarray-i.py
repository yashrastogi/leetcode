class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        csum = sum(nums[:k])
        maxAverage = csum / k
        for i in range(1, len(nums) - k + 1):
            csum = csum - nums[i - 1] + nums[i + k - 1]
            average = csum / k
            maxAverage = max(maxAverage, average)
        return maxAverage
