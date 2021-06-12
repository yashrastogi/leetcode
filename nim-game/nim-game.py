class Solution:
    def canWinNim(self, n: int) -> bool:
        if n in range(1, 3+1): return True
        if n % 4 != 0:
            return True
        else:
            return False