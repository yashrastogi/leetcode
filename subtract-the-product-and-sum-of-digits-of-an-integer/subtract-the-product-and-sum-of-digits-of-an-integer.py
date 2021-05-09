class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        productn = 1
        sumn = 0
        for num in str(n):
            productn *= int(num)
        for num in str(n):
            sumn += int(num)
        return productn-sumn