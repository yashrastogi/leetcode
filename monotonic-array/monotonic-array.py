class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prevNum = nums[0]
        decreasing = False
        for i in range(len(nums)):
            if prevNum == nums[i]:
                continue
            else:
                if prevNum > nums[i]: decreasing = True
                else: decreasing = False
                break
        param = nums[0]
        for num in nums:
            if decreasing and num > param:
                return False
            if not decreasing and num < param:
                return False
            param = num
        return True