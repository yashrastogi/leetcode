class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        rev_nums_counter = defaultdict(list)
        for key in nums_counter:
            rev_nums_counter[nums_counter[key]].append(key)
        max_freq = max(rev_nums_counter.keys())
        ret = []
        for i in reversed(range(1, max_freq+1)):
            for elems in rev_nums_counter[i]:
                if len(ret) < k:
                    ret.append(elems)
                else:
                    break
        return ret