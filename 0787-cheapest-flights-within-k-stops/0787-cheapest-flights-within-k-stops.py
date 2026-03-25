class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(list)
        for f in flights:
            adj[f[0]].append((f[1], f[2]))

        heap = [(0, src, 0)]
        min_stops = [float("inf")] * n
        while heap:
            cost, src, k2 = heappop(heap)
            if src == dst:
                return cost
            if k2 > k or k2 >= min_stops[src]:
                continue
            min_stops[src] = k2
            for nei in adj[src]:
                heappush(heap, (cost + nei[1], nei[0], k2 + 1))
        return -1
