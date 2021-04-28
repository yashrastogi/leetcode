class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsC = Counter(nums)
        for c in numsC:
            if numsC[c] > 1:
                return True
        return False