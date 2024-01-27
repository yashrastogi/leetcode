class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if lengths are equal
        if len(word1) != len(word2):
            return False
        
        # Count frequencies of characters in word1 and word2
        cw1, cw2 = Counter(word1), Counter(word2)
        
        # Iterate over characters in word1
        for key in cw1:
            # Check if character in word1 is not present in word2
            if key not in cw2:
                return False
            
            # Check if frequencies of character in word1 and word2 do not match
            if cw1[key] != cw2[key]:
                # Find a candidate letter to swap by comparing frequencies
                k2 = next((k for k in cw2 if cw2[k] == cw1[key] and cw2[k] != cw1[k]), None)
                if k2 is None:
                    return False
                # Swap frequencies between characters in word2
                cw2[k2], cw2[key] = cw2[key], cw2[k2]
        
        # Check if the frequency counts of characters in both words are equal
        return cw1 == cw2