class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        for num in nums1:
            in2 = 0
            while True:
                if nums2[in2] == num:
                    break
                in2 += 1
            while in2 < len(nums2):
                if nums2[in2] > num:
                    ret.append(nums2[in2])
                    break
                in2 += 1
            if in2 == len(nums2):
                ret.append(-1)
        return ret