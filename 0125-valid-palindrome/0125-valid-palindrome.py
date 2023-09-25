class Solution:
    def isPalindrome(self, news: str) -> bool:
        news = ''.join(filter(str.isalnum, news)).lower()
        i, j = 0, len(news) - 1
        while i < j:
            if news[i] != news[j]:
                return False
            i += 1
            j -= 1
        return True