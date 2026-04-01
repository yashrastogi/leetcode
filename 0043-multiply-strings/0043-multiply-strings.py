class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        b = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                prod = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                csum = b[i + j + 1] + prod

                b[i + j + 1] = csum % 10
                b[i + j] += csum // 10

        return "".join(str(x) for x in b).lstrip("0")
