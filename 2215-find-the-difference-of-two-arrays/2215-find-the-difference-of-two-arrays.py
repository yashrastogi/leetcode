class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setNums1 = set(nums1)
        setNums2 = set(nums2)
        answer = [[], []]
        for num in setNums1:
            if num not in setNums2:
                answer[0].append(num)
        for num in setNums2:
            if num not in setNums1:
                answer[1].append(num)
        return answer