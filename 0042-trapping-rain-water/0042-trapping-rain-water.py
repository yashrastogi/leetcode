class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [height[0]]
        for i in range(1, len(height)):
            left_max.append(max(left_max[-1], height[i]))
        right_max = [height[-1]]
        for i in reversed(range(len(height) - 1)):
            right_max.insert(0, max(right_max[0], height[i]))
        # print(left_max)
        # print(right_max)
        water_trapped = 0
        for i in range(len(height)):
            water_trapped += max(0, min(left_max[i], right_max[i]) - height[i])
        return water_trapped