class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        numTwos = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
            elif nums[i] == 2:
                nums.pop(i)
                numTwos += 1
                i -= 1
            i += 1
        for i in range(numTwos):
            nums.append(2)
        return nums
