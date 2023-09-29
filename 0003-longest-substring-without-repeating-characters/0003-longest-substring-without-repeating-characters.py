class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = hi = 0
        aset = set()
        max_len = 0
        while hi < len(s):
            if s[hi] not in aset:
                aset.add(s[hi])
                hi += 1
            else:
                aset.remove(s[lo])
                lo += 1
            max_len = max(max_len, hi - lo)
        return max_len