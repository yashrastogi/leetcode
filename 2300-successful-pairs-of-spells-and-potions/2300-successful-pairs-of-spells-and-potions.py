class Solution:
    def successfulPairs(self, spells, potions, success):
        pairs = []
        potions.sort()
        for spell in spells:
            count = 0
            searchVal = math.ceil(success / spell)
            if potions[-1] < searchVal:
                pairs.append(0)
                continue
            closeIdx = self.binarySearch(0, len(potions) - 1, searchVal, potions)
            count += len(potions) - closeIdx
            pairs.append(count)
        return pairs

    def binarySearch(self, lo, hi, search, array):
        if lo > hi:
            return hi + 1
        mid = ((hi - lo) // 2) + lo
        if array[mid] < search:
            return self.binarySearch(mid + 1, hi, search, array)
        else:
            return self.binarySearch(lo, mid - 1, search, array)