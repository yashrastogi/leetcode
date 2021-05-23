class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def rec(key, curr_visited):
            nonlocal visited, topoOrder, hasCycle, graph
            if hasCycle: return
            visited.add(key)
            curr_visited.add(key)
            for nbr in graph[key]:
                if nbr not in visited:
                    rec(nbr, curr_visited)
                elif nbr in curr_visited:
                    hasCycle = True
            if not hasCycle:
                topoOrder.append(key)
            curr_visited.remove(key)
            
                    
            
        
        graph = defaultdict(list)
        for prq in prerequisites: graph[prq[0]] += [prq[1]]
        
        
        topoOrder, hasCycle = [], False
        
        visited, curr_visited = set(), set()
        
        for i in range(numCourses):
            if i not in visited:
                rec(i, curr_visited)
            
        if not hasCycle:
            return topoOrder
        else:
            return []