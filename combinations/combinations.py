class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        nums = [*range(1, n+1)]
        
        def rec(num, visited, retLi):
            visited.add(num)
            retLi += [num]
            if len(retLi) == k:
                ret.append(retLi)
                return
            for numx in nums:
                if numx not in visited and numx > num:
                    rec(numx, set(visited), list(retLi))
            
        
        for num in nums:
            rec(num, set(), [])
        return ret