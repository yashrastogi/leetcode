class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])

        arrows = 0
        loc = -1
        for p in points:
            if loc != -1 and p[0] <= loc <= p[1]:
                continue
            arrows += 1
            loc = p[1]

        return arrows
