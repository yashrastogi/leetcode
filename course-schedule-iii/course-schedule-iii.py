class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # we start by sorting the courses array in increasing order of deadline, this is done
        # to ensure that we are able to take up the maximum courses as we traverse the sorted
        # array serially without exhausting the deadline
        
        # we use max heap concept which will always keep the longest duration
        # course within the heap at the top to pop. we replace the longest course
        # with current course, if it is of a shorter duration which could allow us to
        # take more courses as we traverse further
        
        # when pushing/popping from min heap pq, we multiply by -1 to reverse
        # the order of elements in the heap which makes the min heap
        # act as max heap for our usecase
        
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