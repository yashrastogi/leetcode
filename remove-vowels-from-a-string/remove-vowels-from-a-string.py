class Solution:
    def removeVowels(self, s: str) -> str:
        se = set(['a','e','i','o','u'])
        ret = ''
        for c in s:
            if c in se:
                continue
            ret += c
        return ret