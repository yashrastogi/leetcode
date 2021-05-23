class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        curr = nums[0]
        count = 0
        crit = int(len(nums)/3)
        ret = []
        for num in nums:
            if num == curr:
                count += 1
                
            else:
                print(curr, count)
                if count > crit:
                    ret.append(curr)
                curr = num
                count = 1
        if count > crit:
            ret.append(curr)
                
            
        return ret