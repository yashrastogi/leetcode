class Solution:
    def partition(self, s: str) -> [[str]]:
        def backtrack(i: int = 0):
            nonlocal ret, temp
            if i == len(s):
                ret.append(list(temp))
                return
            for length in range(len(s) - i):
                built_string = s[i:i + length + 1]
                if self.is_palindrome(built_string):
                    temp.append(built_string)
                    backtrack(i + length + 1)
                    temp.pop()

        temp = []
        ret = []
        backtrack()
        return ret

    def is_palindrome(self, string: str) -> bool:
        return string == string[::-1]
