class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        ret = []
        for ptr in range(max_len):
            if ptr < len(word1):
                ret.append(word1[ptr])
            if ptr < len(word2):
                ret.append(word2[ptr])
        return "".join(ret)
