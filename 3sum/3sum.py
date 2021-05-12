class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        a = 0
        while a < len(nums)-2:
            if a > 0 and nums[a] == nums[a-1]:
                a += 1
                continue
            target = -1 * nums[a]
            b = a + 1
            c = len(nums) - 1
            while b < c:
                curr_sum = nums[b] + nums[c]
                if curr_sum == target:
                    ret.append([nums[a],nums[b],nums[c]])
                    # break
                    b += 1
                    c -= 1
                    while nums[b] == nums[b-1] and b < c:
                        b += 1
                if curr_sum < target:
                    b += 1
                elif curr_sum > target:
                    c -= 1
            a += 1
        return ret