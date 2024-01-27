class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cw1 = Counter(word1)
        cw2 = Counter(word2)
        for key in cw1:  # iterate through cw1
            if key not in cw2:
                return False
            if cw1[key] != cw2[key]:  # if freq does not match
                for k2 in list(cw2):  # iterate again over all keys in cw2
                    if cw2[k2] == cw1[key] and cw2[k2] != cw1[k2]:  # find a candidate letter to swap by comparing freq
                        temp = cw2[k2]
                        cw2[k2] = cw2[key]
                        cw2[key] = temp
        if cw1 == cw2:
            return True
        return False
