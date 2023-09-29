class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [height[0]]
        for i in range(1, len(height)):
            left_max.append(max(left_max[-1], height[i]))
        right_max = [height[-1]]
        for i in reversed(range(len(height) - 1)):
            right_max.append(max(right_max[-1], height[i]))
        right_max.reverse()
        water_trapped = 0
        for i in range(len(height)):
            water_trapped += min(left_max[i], right_max[i]) - height[i]
        return water_trapped