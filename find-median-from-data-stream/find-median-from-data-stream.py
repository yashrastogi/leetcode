class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def addNum(self, num: int) -> None:
        heappush(self.data, num)

    def findMedian(self) -> float:
        self.data.sort()
        if len(self.data) % 2 != 0:
            return self.data[int(len(self.data)/2)]
        else:
            if len(self.data) == 1:
                return self.data[0]
            else:
                a = int(len(self.data)/2)-1
                b = int(len(self.data)/2)
                return (self.data[a]+self.data[b])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()