class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary(lo, hi):
            if lo > hi: return hi + 1
            mid = (lo + hi) // 2
            if target > nums[mid]:
                res = binary(mid + 1, hi)
                return res
            elif target < nums[mid]:
                res = binary(lo, mid - 1)
                return res
            else:
                return mid
        return binary(0, len(nums) - 1)