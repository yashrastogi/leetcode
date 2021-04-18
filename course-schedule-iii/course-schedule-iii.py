class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        pq = []; heapify(pq)
        time = 0
        
        for course in courses:
            if time + course[0] <= course[1]:
                time += course[0]
                heappush(pq, -1 * course[0])
            elif pq and -1 * pq[0] > course[0]:
                time += course[0] - -1 * heappop(pq)
                heappush(pq, -1 * course[0])
        
        return len(pq)
        