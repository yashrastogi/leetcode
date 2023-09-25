class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''
        s = s.upper()
        for c in s:
            if ord(c) in range(65, 91) or ord(c) in range(48,58):
                news += c
        print(news)
        i, j = 0, len(news) - 1
        while i < j:
            if news[i] != news[j]:
                return False
            i += 1
            j -= 1
        return True