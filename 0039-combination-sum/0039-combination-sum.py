class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrack(idx, arr, target):
            if target == 0:
                ret.append(arr + [])
            if target < 0 or idx >= len(candidates):
                return
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                backtrack(i, arr, target - candidates[i])
                arr.pop()
        backtrack(0, [], target)
        return ret