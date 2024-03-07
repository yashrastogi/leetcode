class Solution:
    def __init__(self):
        self.lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def backtrack(self, digits, idx=0, curr=[""]):
        if idx == len(digits):
            return curr
        ret = []
        for c in curr:
            for char in self.lookup[digits[idx]]:
                ret.append(c + char)
        return self.backtrack(digits, idx + 1, ret)

    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) < 1:
            return []
        return self.backtrack(list(digits))
