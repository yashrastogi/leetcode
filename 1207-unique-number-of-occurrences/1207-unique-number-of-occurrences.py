class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        set_val = set()
        for num in counter:
            if counter[num] in set_val:
                return False
            set_val.add(counter[num])
        return True