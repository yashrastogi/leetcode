class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)):
            # since min left is max height that can pass through
            warehouse[i] = min(warehouse[i], warehouse[i-1])
        
        boxes.sort()
        
        count = 0
        for room in reversed(warehouse):
            if count < len(boxes) and room >= boxes[count]:
                count += 1
        return count