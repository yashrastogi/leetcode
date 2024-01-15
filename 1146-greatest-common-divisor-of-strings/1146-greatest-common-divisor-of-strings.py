class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = gcd(len(str1), len(str2))
        gcd_part = str1[:gcd_len]
        if gcd_part * (len(str1) // gcd_len) == str1 and gcd_part * (len(str2) // gcd_len) == str2:
            return gcd_part
        else:
            return ''