class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        for i in range(n):
            nums[i] = start + 2*i
        xor = 0
        for el in nums:
            xor ^= el
        return xor