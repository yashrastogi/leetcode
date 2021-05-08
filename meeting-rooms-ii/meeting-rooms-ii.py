class Solution:
    def minMeetingRooms(self, i_s: List[List[int]]) -> int:
        rooms = []
        room_count = 0
        i_s.sort(key=lambda x: x[0])
        for el in i_s:
            if len(rooms) == 0:
                heappush(rooms, el[1])
                room_count += 1
            elif rooms[0] <= el[0]:
                t = heappop(rooms)
                heappush(rooms, el[1])
            elif rooms[0] > el[0]:
                heappush(rooms, el[1])
                room_count += 1
                
        return room_count
                