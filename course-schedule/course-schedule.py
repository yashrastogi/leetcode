class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        topoOrder = []
        hasCycle = False
        def rec(key, curr_visited):
            nonlocal graph, visited, hasCycle
            visited.add(key)
            curr_visited.add(key)
            if key in graph:
                for nbr in graph[key]:
                    if nbr not in visited:
                        rec(nbr, curr_visited)
                    elif nbr in curr_visited:
                        hasCycle = True
            topoOrder.append(key)
            curr_visited.remove(key)
        
        graph = {}
        for prq in prerequisites:
            c1, c2 = prq[0], prq[1]
            graph.setdefault(c1, [])
            graph[c1] += [c2]
        
        visited = set()
        curr_visited = set()
        for i in range(numCourses):
            if i not in visited:
                rec(i, curr_visited)
        
        print(topoOrder)
        return not hasCycle