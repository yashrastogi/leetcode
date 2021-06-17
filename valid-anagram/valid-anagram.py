class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        if len(a) != len(b): return False
        ctr_a, ctr_b = Counter(a), Counter(b)
        return ctr_a == ctr_b