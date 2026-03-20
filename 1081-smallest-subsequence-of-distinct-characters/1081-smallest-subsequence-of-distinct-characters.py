class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        charset = set()
        for i, ch in enumerate(s):
            if ch in charset:
                continue
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                charset.remove(stack[-1])
                stack.pop()
            stack.append(ch)
            charset.add(ch)
        return "".join(stack)
