class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def calcSum(end, items_to_take):
            start = max(0, end - items_to_take + 1)
            return ((end - start + 1) * (start + end)) // 2

        heap = []
        [heappush_max(heap, (i, 1)) for i in inventory]
        profit = 0
        while orders > 0 and heap[0][0] > 0:
            top_pile, count = heappop_max(heap)
            while heap and heap[0][0] == top_pile:
                count += heap[0][1]
                heappop_max(heap)
            next_pile = heap[0][0] if heap else 0
            items_to_take = min(count, orders)

            levels_to_sell = 1
            if items_to_take != orders:
                levels_to_sell = max(1, min(orders // count, top_pile - next_pile))
            orders -= items_to_take * levels_to_sell
            profit = (profit + items_to_take * calcSum(top_pile, levels_to_sell)) % (
                10**9 + 7
            )
            heappush_max(heap, (top_pile - levels_to_sell, count))
        return profit
