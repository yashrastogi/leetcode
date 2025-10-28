class Solution:
    def nextPermutation(T, nums: List[int]) -> None:
        n = len(nums)

        def reverse(nums):
            i = 0
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        def fix_window(i):
            print(i, n, nums[i : n])
            for x in reversed(range(i, n - 1)):
                if nums[x] < nums[x + 1]:
                    # if increasing trend broke at x then find next larger el to right of x
                    min_i = x + 1
                    for z in range(x + 1, n):
                        if nums[z] <= nums[min_i] and nums[z] > nums[x]:
                            min_i = z
                    # swap with next smallest successor
                    nums[x], nums[min_i] = nums[min_i], nums[x]
                    print(i, n, nums[i : n])
                    # reverse rest in window to create lexiy smallest window
                    left, right = x + 1, n - 1
                    while left < right:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
                        right -= 1
                    print(i, n, nums[i : n])
                    break

        if len(nums) < 2:
            return
        last_seen_max = nums[n - 1]
        for i in reversed(range(len(nums))):
            if nums[i] < last_seen_max:
                fix_window(i)
                break
            last_seen_max = max(last_seen_max, nums[i])
            i -= 1
        if i == -1:
            reverse(nums)
