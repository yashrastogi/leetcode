from pprint import pprint


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manD(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        n = len(points)
        visited = set()
        mst_edges = []
        cost = 0
        min_heap = [(0, 0, -1)]  # weight,node,parent
        while len(visited) < n:
            w, no, p = heappop(min_heap)
            if no in visited:
                continue
            cost += w
            visited.add(no)
            if p != -1:
                mst_edges.append((w, (points[p], points[no])))
            for i in range(n):
                if i not in visited:
                    heappush(min_heap, (manD(points[no], points[i]), i, no))
        return cost
