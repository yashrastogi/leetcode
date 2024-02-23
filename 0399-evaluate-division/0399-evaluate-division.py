class Solution:
    def calcEquation(self, equations, values, queries):
        visited = set()

        def dfs(curr, dest):
            visited.add(curr)
            if curr == dest: return 1
            ret_val = -1
            for d in graph[curr]:
                if dest == d[0]:
                    # print(curr, "->", d[0], "(", d[1], ")", end="\t")
                    # print("END")
                    return d[1]
                elif d[0] not in visited:
                    # print(curr, "->", d[0], "(", d[1], ")", end="\t")
                    test = dfs(d[0], dest)
                    if test != -1:
                        ret_val = d[1] * test
            # print("END")
            return ret_val

        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            graph[eq[0]] += [(eq[1], values[i])]
            graph[eq[1]] += [(eq[0], 1 / values[i])]
        res = []
        # import pprint; pprint.pprint(graph)
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                res.append(-1)
            else:
                # print(q)
                res.append(dfs(q[0], q[1]))
                visited.clear()
                # print("\n" * 3)
        return res
