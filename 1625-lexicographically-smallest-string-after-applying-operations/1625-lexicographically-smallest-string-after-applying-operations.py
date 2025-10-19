class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def rotateNum(num_str, times):
            num_l = list(num_str)
            for _ in range(times):
                temp = num_l.pop(-1)
                num_l.insert(0, temp)
            return "".join(num_l)

        def addDigit(num_str, n2):
            num_l = list(num_str)
            for i in range(1, len(num_l), 2):
                num_l[i] = str((int(num_l[i]) + n2) % 10)
            return "".join(num_l)

        def dfs(s, visited=set()):
            if s in visited:
                return
            visited.add(s)
            dfs(rotateNum(s, b), visited)
            dfs(addDigit(s, a), visited)
            return visited

        return min(dfs(s))
