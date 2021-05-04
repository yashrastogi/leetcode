class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ret = []
        idx = 0
        while idx < len(nums):
            i = idx + 1
            if i == len(nums):
                i = 0
            flag = False
            while i != idx:
                if nums[i] > nums[idx]:
                    flag = True
                    ret.append(nums[i])
                    break
                if i + 1 < len(nums):
                    i += 1
                elif i + 1 == len(nums):
                    i = 0
            if not flag:
                ret.append(-1)
            idx+=1
            
        return ret