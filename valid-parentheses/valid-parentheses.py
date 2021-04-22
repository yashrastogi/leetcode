class Solution:
    def isValid(self, s: str) -> bool:
        deq = deque()
        br = {']': '[', '}': '{', ')': '('}
        for c in s:
            if c in br.values():
                deq.append(c)
            elif deq:
                if br[c] != deq.pop():
                    return False
            else:
                return False
        if deq:
            return False
        return True