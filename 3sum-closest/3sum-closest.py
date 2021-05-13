class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def m(a, b):
            if a > b: return a-b
            else: return b-a
        
        nums.sort()
        ret_sum=0
        min_diff = float('inf')
        
        for i in range(len(nums)-2):
            a = i + 1
            b = len(nums) - 1
            
            while a < b:
                sum = nums[i] + nums[a] + nums[b]
                if m(sum,target) < min_diff:
                    min_diff = m(sum,target)
                    ret_sum = sum
                if sum > target:
                    b -= 1
                elif sum < target:
                    a += 1
                else:
                    break
        
        return ret_sum