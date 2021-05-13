class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        len_long = 0
        for i in range(len(s)):
            a = i
            curr_cnt = {}
            while a < len(s):
                curr_cnt.setdefault(s[a], 0)
                curr_cnt[s[a]] += 1
                if max(curr_cnt.values()) > 1:
                    break
                else:
                    a += 1
        
            len_long = max(len_long, a-i)
        
        return len_long