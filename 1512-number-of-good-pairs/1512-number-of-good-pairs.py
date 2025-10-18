class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = defaultdict(list)
        count = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                count += len(seen[nums[i]])
            seen[nums[i]].append(i)
        return count