class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        rets = []
        for key in count.keys():
            if count[key] > len(nums) / 3:
                rets.append(key)
        return rets
