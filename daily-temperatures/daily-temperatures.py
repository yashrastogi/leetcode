class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(T)
        
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                curr = stack.pop()
                ret[curr] = i - curr
            stack.append(i)
            
        return ret