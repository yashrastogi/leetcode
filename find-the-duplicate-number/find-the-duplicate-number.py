class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = lambda x: nums[x]
        
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = f(slow)
            fast = f(f(fast))
            if slow == fast:
                break
        
        slow = nums[0]
        while True:
            if slow == fast:
                break
            slow = f(slow)
            fast = f(fast)
        return fast
            

            
        
    