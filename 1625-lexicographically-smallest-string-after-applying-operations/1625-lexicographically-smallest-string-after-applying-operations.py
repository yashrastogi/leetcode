class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def rotateNum(num, times):
            if times <= 0:
                return num
            last_digit = num % 10
            digits = 0
            temp = num
            while temp > 0:
                temp = temp // 10
                digits += 1
            new_num = (num // 10) + last_digit * pow(10, digits - 1)
            return rotateNum(new_num, times - 1)

        def addDigit(num, n2):
            num_l = str(num).split()