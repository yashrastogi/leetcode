class Solution:
    def countKeyChanges(self, s: str) -> int:
        last_used = s[0].lower()
        counter = 0
        for i in range(1, len(s)):
            c = s[i].lower()
            if c != last_used:
                counter += 1
            last_used = c
        return counter
        