class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_positive, max_negative = 1, 1
        result = nums[0]
        
        for num in nums:
            if num == 0:
                result = max(result, 0)
                max_positive, max_negative = 1, 1
                continue
            temp = max_positive * num
            max_positive = max(max_positive * num, max_negative * num, num)
            max_negative = min(temp, max_negative * num, num)
            result = max(result, max_positive)
            
        
        return result