class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_locations = []
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowel_locations.append(i)
        print(vowel_locations)
        sc = list(s)
        for i in range(len(vowel_locations) // 2):
            print(i)
            num1 = vowel_locations[i]
            num2 = vowel_locations[-i-1]
            temp = sc[num1]
            sc[num1] = sc[num2]
            sc[num2] = temp
        return ''.join(sc)