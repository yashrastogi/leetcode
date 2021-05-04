class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        resli = []
        
        def dfs(candidates, res, target):
            for x, i in enumerate(candidates):
                if i > target:
                    break
                elif i == target:
                    resli.append(res)
                    resli[-1].append(i)
                else:
                    dfs(candidates[x:] ,res+[i], target-i)
        
        dfs(candidates, [], target)

        return resli
    