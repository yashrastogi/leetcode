class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == cand:
                count += 1
            else:
                count -= 1
            if count == 0:
                cand = nums[i]
                count = 1
        
        count_cand = 0
        for num in nums:
            if num == cand:
                count_cand += 1
        
        if count_cand >= int(len(nums)/2):
            return cand