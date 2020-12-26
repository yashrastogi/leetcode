class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seta = set()
        for num in nums:
            if num in seta:
                return num
            else:
                seta.add(num)
