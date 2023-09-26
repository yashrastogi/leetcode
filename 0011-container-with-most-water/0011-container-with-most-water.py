class Solution:
    def maxArea(self, arr: List[int]) -> int:
        maxAr = 0
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            area = (hi - lo) * min(arr[lo], arr[hi])
            maxAr = max(maxAr, area)
            if arr[lo] < arr[hi]:
                lo += 1
            else:
                hi -= 1
        return maxAr