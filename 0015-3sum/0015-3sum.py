class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        print(nums)
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            i = x + 1
            j = len(nums) - 1
            while i < j:
                csum = nums[i] + nums[j] + nums[x]
                if csum == 0:
                    temp = [nums[x], nums[i], nums[j]]
                    ret.append(temp)
                    i += 1
                    j -= 1
                    while i < len(nums) and nums[i] == nums[i - 1]:
                        i += 1
                    while j >= 0 and nums[j] == nums[j+1]:
                        j -= 1
                elif csum < 0:
                    i += 1
                elif csum > 0:
                    j -= 1
        return ret