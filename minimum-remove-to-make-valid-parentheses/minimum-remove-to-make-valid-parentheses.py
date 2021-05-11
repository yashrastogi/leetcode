class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) == 0:
                    s = s[:i] + '0' + s[i+1:]
                else:
                    stack.pop()
        
        if len(stack) != 0:
            for num in stack:
                s = s[:num] + '0' + s[num+1:]
        
        return s.replace('0','')