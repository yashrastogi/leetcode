class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        heap = []
        for key in nums_counter:
            heappush(heap, (-nums_counter[key], key))
        ret = []
        for i in range(k):
            ret.append(heappop(heap)[1])
        return ret