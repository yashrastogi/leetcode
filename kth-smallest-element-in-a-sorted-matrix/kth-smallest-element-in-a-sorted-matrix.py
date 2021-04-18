class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        li = []; heapify(li)
        for m in matrix:
            for i in m:
                heappush(li, -1 * i)
                if len(li) > k:
                    heappop(li)
        return -1 * heappop(li)
                