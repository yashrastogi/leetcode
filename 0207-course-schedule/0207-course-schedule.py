class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def checkCycle(i):
            nonlocal visited, visited_curr
            visited.add(i)
            visited_curr.add(i)
            for nbr in graph[i]:
                if nbr not in visited and checkCycle(nbr):
                    return True
                elif nbr in visited_curr:
                    return True
            visited_curr.remove(i)
            return False
        
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])
        visited = set()
        visited_curr = set()
        for i in range(numCourses):
             if i not in visited:
                    if checkCycle(i):
                        return False
        return True