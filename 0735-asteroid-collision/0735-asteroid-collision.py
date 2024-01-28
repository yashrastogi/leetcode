class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(a):
            if a[i] > 0:
                stack.append(a[i])
            else:
                if not stack:
                    stack.append(a[i])
                else:
                    while stack and stack[-1] > 0 and stack[-1] < abs(a[i]):
                        stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(a[i])
                    elif stack[-1] == abs(a[i]):
                        stack.pop()
            i += 1
        return stack
