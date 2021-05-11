class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        total = set()
        def recurse(li, count_dict):
            nonlocal total
            if len(li) == len(nums):
                total.add(tuple(li))
                return
            for i in count_dict:
                if count_dict[i] > 0:
                    dup = dict(count_dict)
                    dup[i] -= 1
                    recurse(li + [i], dup)
               
        recurse([], Counter(nums))
        return list(total)