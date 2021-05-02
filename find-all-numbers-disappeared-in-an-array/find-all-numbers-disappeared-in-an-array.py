class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        keys = nums_counter.keys()
        ret = []
        for i in range(1, len(nums)+1):
            if i not in keys:
                ret.append(i)
        return ret
            