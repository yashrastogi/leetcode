class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo <= hi:
            k = (hi + lo) // 2
            kSum = sum(math.ceil(pile / k) for pile in piles)
            if kSum <= h:
                hi = k - 1
            elif kSum > h:
                lo = k + 1
        return lo

s = Solution()
f = open('user.out', 'w')
for piles, h in zip(map(loads, stdin), map(loads, stdin)):
    f.write(dumps(s.minEatingSpeed(piles, h)).replace(' ', '') + '\n')
exit()