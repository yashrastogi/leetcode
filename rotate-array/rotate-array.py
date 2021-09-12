class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        buffer = []
        for i in range(len(nums) - 1, len(nums) - 1 - k, -1):
            nums.insert(0, nums.pop())