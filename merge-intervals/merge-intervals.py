class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = []
        
        i = 0
        while i < len(intervals):
            cur = intervals[i]
            j = i+1
            while j < len(intervals) and cur[1] >= intervals[j][0]:
                cur[1] = max(cur[1], intervals[j][1])
                j += 1
                i += 1
            ret.append(cur)
            i += 1
        
        return ret