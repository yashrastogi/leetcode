class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        for key in nums_counter:
            if nums_counter[key] == 1:
                return key