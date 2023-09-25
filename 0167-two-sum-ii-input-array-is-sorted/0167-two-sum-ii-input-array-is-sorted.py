class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            csum = numbers[i] + numbers[j]
            if csum == target:
                return [i + 1, j + 1]
            elif csum < target:
                i += 1
            elif csum > target:
                j -= 1
        return None