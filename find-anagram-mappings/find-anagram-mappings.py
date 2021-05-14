class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di_nums2 = {}
        for i, num in enumerate(nums2):
            di_nums2.setdefault(num, [])
            di_nums2[num] += [i]
        
        
        ret = []
        for i, num in enumerate(nums1):
            ret.append(di_nums2[num].pop())
            
        return ret