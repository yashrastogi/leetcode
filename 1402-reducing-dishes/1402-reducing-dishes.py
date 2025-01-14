class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        @functools.cache
        def recurse(i=0, dishes=0):
            if i >= len(satisfaction):
                return 0
            return max(
                (dishes + 1) * satisfaction[i] + recurse(i + 1, dishes + 1),
                recurse(i + 1, dishes),
            )

        return recurse()
