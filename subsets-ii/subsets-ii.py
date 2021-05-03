class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def rec(idx, li, ret):
            if idx == len(nums):
                return
            li2 = li+[nums[idx]]
            ret.append(li2)
            rec(idx+1, li, ret)
            rec(idx+1, li2, ret)    
        
        ret = [[]]
        nums.sort()
        rec(0, [], ret)
        ret2 = []
        for i in range(len(ret)):
            flag = True
            for j in range(i+1, len(ret)):
                if ret[i] == ret[j]:
                    flag = False
                    break
            if flag:
                ret2.append(ret[i])
        return ret2