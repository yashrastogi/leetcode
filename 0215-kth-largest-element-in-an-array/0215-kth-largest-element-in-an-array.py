class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        ret = float("inf")
        for i in range(k):
            ret = -heappop(nums)
        return ret
