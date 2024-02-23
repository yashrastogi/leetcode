class Solution:
    def calcEquation(self, equations, values, queries):
        visited = set()

        def dfs(curr, dest):
            visited.add(curr)
            if curr == dest:
                return 1
            ret_val = -1
            for d in graph[curr]:
                if d[0] not in visited:
                    test = dfs(d[0], dest)
                    if test != -1:
                        ret_val = d[1] * test
            return ret_val

        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            graph[eq[0]] += [(eq[1], values[i])]
            graph[eq[1]] += [(eq[0], 1 / values[i])]
        res = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                res.append(-1)
            else:
            res.append(dfs(q[0], q[1]))
            visited.clear()
        return res
