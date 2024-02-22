class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()

        def dfs(curr):
            visited.add(curr)
            change_count = 0
            for city in graph[curr]:
                if city[0] not in visited:
                    change_count += dfs(city[0]) + city[1]
            return change_count

        graph = defaultdict(list)
        for i, j in connections:
            graph[j] += [(i, 0)]  # reverse edge
            graph[i] += [(j, 1)]  # forward edge

        return dfs(0)
