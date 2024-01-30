class RecentCounter:
    def __init__(self):
        self.storage = []

    def ping(self, t: int) -> int:
        self.storage.append(t)
        low = t - 3000
        while self.storage[0] < low:
            self.storage.pop(0)
        return len(self.storage)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)