class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u] += [(w, v)]
            
        pq = [(0, k)]
        distance = collections.defaultdict(lambda: float('inf'))
        while pq:
            d, node = heappop(pq)
            if node in distance:
                continue
            distance[node] = d
            for nbr_pair in graph[node]:
                dx, nodex = nbr_pair[0] + d, nbr_pair[1]
                if nodex not in distance:
                    heappush(pq, (dx, nodex))
        
        max_distance = 0
        for i in range(1, n+1):
            if i != k:
                if i not in distance:
                    return -1
                else:
                    max_distance = max(max_distance, distance[i])
        return max_distance
                
                