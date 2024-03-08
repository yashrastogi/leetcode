class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        def backtrack(times: int, total: int, curr: [int]):
            if times == k:
                if total == n:
                    res.append(curr.copy())
                return
            elif total >= n:
                return
            for num in range(curr[-1] + 1 if curr else 1, 10):
                curr.append(num)
                backtrack(times + 1, total + num, curr)
                curr.pop()

        res = []
        tempCurr = []
        backtrack(0, 0, tempCurr)
        return res
