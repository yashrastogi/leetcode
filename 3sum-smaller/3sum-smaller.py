class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        count = 0
        for a in range(len(nums)-2):
            b = a+1
            c = len(nums)-1
            while b < c:
                curr_sum = nums[a] + nums[b] + nums[c]
                if curr_sum < target:
                    count += c - b
                    b+=1
                else:
                    c-=1
        return count