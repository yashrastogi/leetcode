class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heappush(heap, (-1 * (nums1[i]+nums2[j]), (nums1[i], nums2[j])))
                if len(heap) > k:
                    heappop(heap)
        
        ret = []
        for _ in range(len(heap)):
            ret.append(heappop(heap)[1])
        return ret