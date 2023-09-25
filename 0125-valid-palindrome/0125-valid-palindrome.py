class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        for c in s:
            if not (ord(c) in range(65, 91) or ord(c) in range(48,58)):
                s = s.replace(c, '')
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True