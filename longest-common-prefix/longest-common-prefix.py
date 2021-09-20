class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minWord, minLen = "", float("inf")

        for word in strs:
            lenw = len(word)
            if lenw < minLen:
                minLen = lenw
                minWord = word

        continueLoop = True
        ret = ""
        for idx, char in enumerate(minWord):
            for word in strs:
                if word[idx] != char:
                    continueLoop = False
                    break
            if continueLoop:
                ret += char
            else:
                break
        return ret