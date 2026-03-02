class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visited_curr = set()

        def checkCycle(i, visited=visited, visited_curr=visited_curr):
            visited.add(i)
            visited_curr.add(i)
            for nbr in graph[i]:
                if nbr in visited_curr or (nbr not in visited and checkCycle(nbr)):
                    return True
            visited_curr.remove(i)
            return False

        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])
        for i in range(numCourses):
            if i not in visited:
                if checkCycle(i):
                    return False
        return True
