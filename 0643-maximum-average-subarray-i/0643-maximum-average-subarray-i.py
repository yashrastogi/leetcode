class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        csum = sum(nums[:k])
        max_csum = csum
        for i in range(1, len(nums) - k + 1):
            csum = csum - nums[i - 1] + nums[i + k - 1]
            if csum > max_csum:
                max_csum = csum
        return max_csum / k
