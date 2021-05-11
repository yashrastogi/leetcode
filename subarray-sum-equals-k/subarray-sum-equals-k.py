class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        count = 0
        sum = 0
        '''
        intuition regarding the O(n) solution is we're recording earlier cumulative sums (cumsums) so that when we encounter the latest cumsum that is k away from an earlier cumsum, we know to increment count. We record a "number of times" for earlier values, ensuring we capture all extended up-and-down sequences where elements cancel.
        '''
        for num in nums:
            sum += num
            if sum - k in hashmap:
                count += hashmap[sum - k]
            hashmap[sum] = hashmap.setdefault(sum, 0) + 1
                
        return count
            