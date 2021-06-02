class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        RED, BLUE, GREEN = 0, 1, 2
        
        @cache
        def rec(idx, cost, last_color):
            if(idx < 0): return cost
            minCost = float('inf')
            for color in [RED, BLUE, GREEN]:
                if color == last_color: continue
                minCost = min(minCost, rec(idx - 1, cost + costs[idx][color], color))
            return minCost
        
        return rec(len(costs)-1, 0, -1)