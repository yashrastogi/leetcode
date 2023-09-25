class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        for x in range(len(nums)):
            i = x + 1
            j = len(nums) - 1
            while i < len(nums) and i < j:
                csum = nums[i] + nums[j] + nums[x]
                if csum == 0:
                    temp = (nums[x], nums[i], nums[j])
                    if temp not in ret:
                        ret.add(temp)
                    i += 1
                    j -= 1
                elif csum < 0:
                    i += 1
                elif csum > 0:
                    j -= 1
        return list(ret)