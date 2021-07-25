class Solution:
    def maxArea(self, height: List[int]) -> int:
        # calcArea = lambda x1, y1, x2, y2: \
        #     (max(x1, x2) - min(x1, x2)) * (max(y1, y2) - min(y1, y2))
        # calcWidth = lambda i1, i2: max(i1, i2) - min(i1, i2)
        
        i, j = 0, len(height) - 1
        maxAr = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if maxAr < area:
                maxAr = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return maxAr
              