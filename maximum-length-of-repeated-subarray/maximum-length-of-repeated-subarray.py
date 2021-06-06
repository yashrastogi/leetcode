import pprint

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1) + 1, len(nums2) + 1
        dp = [[-1] * l2 for _ in range(l1)]
        
        def _bottomUp(l1x, l2x):
            nonlocal nums1, nums2, dp
            if l1x == 0 or l2x == 0:
                return 0
            if (t := dp[l1x][l2x]) != -1:
                return t
            if nums1[l1x - 1] == nums2[l2x - 1]:
                ret = 1 + _bottomUp(l1x - 1, l2x - 1)
            else:
                ret = 0
            dp[l1x][l2x] = ret
            return ret
        
        def bottomUp(l1, l2):
            maxLength = 0
            for i in range(l1):
                for j in range(l2):
                    maxLength = max(maxLength, _bottomUp(i, j))
            return maxLength
        
        def topDown(l1, l2):
            for i in range(l1):
                for j in range(l2):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    elif nums1[i - 1] == nums2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 0
            maxLength = 0
            for i in range(l1):
                for j in range(l2):
                    maxLength = max(maxLength, dp[i][j])
            return maxLength
                
        return topDown(l1, l2)