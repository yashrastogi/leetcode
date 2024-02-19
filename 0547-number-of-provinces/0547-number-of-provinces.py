class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)

        def dfs(city_num):
            if city_num in visited:
                return
            visited.add(city_num)
            for j in range(n):
                if isConnected[city_num][j] == 1:
                    dfs(j)

        provinces = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces
