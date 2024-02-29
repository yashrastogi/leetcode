class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        z = sorted(zip(nums1, nums2), key=lambda x: x[1])
        n = len(nums1)
        minHeap = []
        maxScore = -1
        total_sum = 0

        for i, el in enumerate(reversed(z)):
            heapq.heappush(minHeap, el[0])
            total_sum += el[0]
            if len(minHeap) >= k:
                maxScore = max(maxScore, total_sum * el[1])
                total_sum -= heapq.heappop(minHeap)

        return maxScore


s = Solution()
f = open("user.out", "w")

for nums1, nums2, k in zip(map(loads, stdin), map(loads, stdin), map(loads, stdin)):
    f.write(dumps(s.maxScore(nums1, nums2, k)).replace(" ", "") + "\n")
exit()
