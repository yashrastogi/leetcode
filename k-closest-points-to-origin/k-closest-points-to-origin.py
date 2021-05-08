class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closest = []
        def distance(p1, p2):
            a, b = pow(p1[0] - p2[0], 2), pow(p1[1] - p2[1], 2)
            return math.sqrt(a+b)
        
        heap = []
        for pt in points:
            heappush(heap, (-1*distance(pt, [0,0]), pt[0], pt[1]))
            
        for e in heapq.nlargest(k, heap):
            k_closest.append([e[1], e[2]])
        
        return k_closest
            
            