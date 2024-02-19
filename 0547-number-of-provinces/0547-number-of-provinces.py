class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(city_num):
            if city_num in visited:
                return
            visited.add(city_num)
            for j in range(len(isConnected[city_num])):
                if isConnected[city_num][j] == 1:
                    dfs(j)

        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces
