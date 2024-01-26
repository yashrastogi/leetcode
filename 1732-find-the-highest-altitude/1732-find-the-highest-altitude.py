class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        max_alt = 0
        for alt in gain:
            prefix_sum += alt
            max_alt = max(max_alt, prefix_sum, 0)
        return max_alt