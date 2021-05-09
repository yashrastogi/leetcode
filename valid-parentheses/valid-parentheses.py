class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        br = {']': '[', '}': '{', ')': '('}
        for c in s:
            if c in br.values():
                stack.append(c)
            elif stack:
                if br[c] != stack.pop():
                    return False
            else:
                return False
        if stack:
            return False
        return True