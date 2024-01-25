class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = j = 0
        zeroes = 0
        longestOneSubsequence = 0
        usedPowerup = False
        while j < len(nums):
            if nums[j] == 1:
                if usedPowerup:
                    longestOneSubsequence = max(longestOneSubsequence, j - i)
                if not usedPowerup:
                    longestOneSubsequence = max(longestOneSubsequence, j - i + 1)
                j += 1
            elif nums[j] == 0:
                if not usedPowerup:
                    longestOneSubsequence = max(longestOneSubsequence, j - i)
                    usedPowerup = True
                    j += 1
                else:
                    while nums[i] != 0:
                        i += 1
                    i += 1
                    usedPowerup = False
        if longestOneSubsequence == len(nums):
            return len(nums) - 1
        else:
            return longestOneSubsequence