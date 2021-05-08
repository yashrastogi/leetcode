class Solution:
    def trap(self, hi: List[int]) -> int:
        water_units = 0
        for i in range(0, len(hi)):
            left = hi[:i]
            right = hi[i+1:]
            min_max = min(max(left, default=0), max(right, default=0))
            if min_max > hi[i]:
                water_units += min_max - hi[i]
        return water_units