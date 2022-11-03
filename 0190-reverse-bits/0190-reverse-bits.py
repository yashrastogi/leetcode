class Solution:
    def reverseBits(self, n: int) -> int:
        s = "{0:b}".format(n)
        while len(s) < 32:
            s = '0' + s
        a = s[::-1]
        return int(a, 2)
        