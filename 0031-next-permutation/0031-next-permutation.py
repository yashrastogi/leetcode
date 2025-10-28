class Solution:
    def nextPermutation(T, nums: List[int]) -> None:
        n = len(nums)

        def reverse():
            i, j = 0, n - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        def fix_window(i):
            # if increasing trend broke at i then find next larger el to right of i
            min_i = i + 1
            for z in range(i + 1, n):
                if nums[z] <= nums[min_i] and nums[z] > nums[i]:
                    min_i = z
            # swap with next smallest successor
            nums[i], nums[min_i] = nums[min_i], nums[i]
            # reverse rest in window to create lexiy smallest window
            left, right = i + 1, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if len(nums) < 2:
            return
        last_seen_max = nums[n - 1]
        for i in reversed(range(len(nums))):
            if nums[i] < last_seen_max:
                fix_window(i)
                break
            elif i == 0:
                reverse()
            last_seen_max = max(last_seen_max, nums[i])
