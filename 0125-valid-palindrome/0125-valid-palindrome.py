class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''
        s = s.lower()
        for c in s:
            if ord(c) in range(ord('a'), ord('z')+1) or ord(c) in range(ord('0'),ord('9') + 1):
                news += c
        i, j = 0, len(news) - 1
        while i < j:
            if news[i] != news[j]:
                return False
            i += 1
            j -= 1
        return True