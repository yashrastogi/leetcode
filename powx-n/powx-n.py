class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        
        power = self.myPow(x*x, int(n/2)) # x^n = (x^2)^(n/2)
        
        if n % 2 == 0:
            return power
        
        if n < 0:
            return power / x
        
        return x * power
