class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                break
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
        return (i+1, j+1)