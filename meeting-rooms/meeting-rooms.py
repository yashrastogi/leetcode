class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals):
            j = i+1
            while j < len(intervals):
                if intervals[j][0] < intervals[i][1]:
                    return False
                j+=1
            i+=1
        return True