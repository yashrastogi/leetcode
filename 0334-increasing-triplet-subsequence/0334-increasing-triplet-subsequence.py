class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float("inf")
        for num in nums:
            if min1 >= num:
                min1 = num
            elif min2 >= num:
                min2 = num
            else:
                # min2 will only be set when there exists a number min1 less than min2 existing before it
                # so printing it in seq min1 min2 curr might not yield correct output even though the algorithm
                # is sound
                return True
        return False
