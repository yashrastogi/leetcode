class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort(key=lambda x: x[0])
        di = {}
        for log in logs:
            birth, death = log[0], log[1]
            for i in range(birth, death):
                di.setdefault(i, 0)
                di[i] += 1
        return max(di.items(), key=lambda x: x[1])[0]