class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        max_alt = 0
        for alt in gain:
            prefix_sum += alt
            if prefix_sum > max_alt:
                max_alt = prefix_sum
        return max(0, max_alt)