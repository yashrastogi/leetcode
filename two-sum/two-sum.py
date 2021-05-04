class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxDict = {}
        for i, num in enumerate(nums):
            idxDict[num] = i
        for i, num in enumerate(nums):
            comp = target - num
            if comp in idxDict and idxDict[comp] != i:
                return [i, idxDict[comp]]
        return [-1, -1]