class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        max_candies = max(candies)
        ret = []
        for nc in candies:
            if nc + extraCandies >= max_candies:
                ret.append(True)
            else:
                ret.append(False)
        return ret
