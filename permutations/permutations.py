class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        ret = []
        
        def rec(num, nums_set, retLi):
            nums_set_dup = set(nums_set)
            nums_set_dup.remove(num)
            retLi += [num]
            if len(nums_set_dup) == 0:
                ret.append(retLi)
            for numi in nums_set_dup:
                rec(numi, nums_set_dup, list(retLi))
            
        
        for num in nums:
            rec(num, nums_set, [])
        return ret