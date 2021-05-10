class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set()
        temp = 0
        for i in range(n):
            temp = heappop(heap)
            for factor in [2,3,5]:
                if temp * factor not in visited:
                    heappush(heap, temp * factor)
                    visited.add(temp * factor)
        return temp