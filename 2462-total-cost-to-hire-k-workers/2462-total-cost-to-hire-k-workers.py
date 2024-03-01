class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        totalCost = 0
        heap = []
        p1, p2 = 0, len(costs) - 1
        while p1 < candidates:
            heappush(heap, (costs[p1], p1))
            p1 += 1
        while p2 >= len(costs) - candidates and p2 >= p1:
            heappush(heap, (costs[p2], p2))
            p2 -= 1
        for _ in range(k):
            minElement = heappop(heap)
            totalCost += minElement[0]
            if minElement[1] < p1 and p1 <= p2:
                heappush(heap, (costs[p1], p1))
                p1 += 1
            elif p2 >= p1:
                heappush(heap, (costs[p2], p2))
                p2 -= 1
        return totalCost
