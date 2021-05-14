class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
                max_depth = max(max_depth, len(stack))
            elif c == ')':
                stack.pop()
            
        return max_depth
                
                