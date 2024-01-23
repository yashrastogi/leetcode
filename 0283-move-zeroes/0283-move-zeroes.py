class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ptr2 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[ptr2] = nums[ptr2], nums[i]
                ptr2 += 1
