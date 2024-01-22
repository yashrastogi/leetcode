class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count_zero = 0
        while i < len(nums):
            if i + count_zero >= len(nums):
                break
            if nums[i] == 0:
                count_zero += 1
                for j in range(i + 1, len(nums)):
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                print(i, count_zero, nums)
            if nums[i] != 0:
                i += 1