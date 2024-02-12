class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked_rooms = set()

        def exploreRooms(room):
            if room in unlocked_rooms:
                return
            unlocked_rooms.add(room)
            for key in rooms[room]:
                exploreRooms(key)

        exploreRooms(0)
        return len(unlocked_rooms) == len(rooms)
