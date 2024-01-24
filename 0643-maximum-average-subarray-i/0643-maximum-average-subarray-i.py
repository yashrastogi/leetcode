class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        csum = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            csum2 = csum - nums[i - 1] + nums[i + k - 1]
            csum = max(csum, csum2)
        return csum/k
