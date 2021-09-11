# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        def binary(lo, hi):
            if lo > hi: return
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                return binary(lo, mid - 1) or mid
            else:
                return binary(mid + 1, hi)
        return binary(1, n)
        