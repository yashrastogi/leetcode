class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(lo, curr):
            if(len(curr) > len(nums)):
                return
            
            ret.append(list(curr))
            for i in range(lo, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
            
        backtrack(0, [])
        return ret
    
            