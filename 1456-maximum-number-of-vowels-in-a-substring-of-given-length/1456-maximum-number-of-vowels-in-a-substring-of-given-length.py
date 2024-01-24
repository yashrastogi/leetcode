class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_list = ["a", "e", "i", "o", "u"]
        vowels_count = 0
        for i in range(k):
            if s[i] in vowels_list:
                vowels_count += 1
        max_vowels_count = vowels_count
        start = 0
        for end in range(k, len(s)):
            if s[end] in vowels_list:
                vowels_count += 1
            if s[start] in vowels_list:
                vowels_count -= 1
            start += 1
            max_vowels_count = max(max_vowels_count, vowels_count)
        return max_vowels_count
