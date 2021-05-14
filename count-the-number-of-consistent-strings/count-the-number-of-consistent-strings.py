class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_set = set(allowed)
        count = 0
        for word in words:
            flag = True
            for c in word:
                if c not in allow_set:
                    flag = False
                    break
            if flag:
                count += 1
        
        return count