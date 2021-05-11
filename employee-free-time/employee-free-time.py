"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        pi = lambda i: print(f"[{i.start} - {i.end}]")
        temp = [i for c in schedule for i in c]
        temp.sort(key=lambda x: x.start)
        
        temp2 = []
        i = 0
        while i < len(temp):
            interval = temp[i]
            j = i+1
            while j < len(temp) and interval.end >= temp[j].start:
                interval.end = max(interval.end, temp[j].end)
                j += 1
                i += 1
            temp2.append(interval)
            i += 1
            
        # for c in temp2: pi(c)
        temp3 = []
        for i in range(len(temp2)-1):
            temp3.append(Interval(temp2[i].end, temp2[i+1].start))
        return temp3
            