class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc = max(candies)
        ret = []
        for c in candies:
            if c + extraCandies >= maxc:
                ret.append(True)
            else:
                ret.append(False)
        return ret