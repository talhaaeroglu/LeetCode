class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set([0])
        stack = [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited_rooms:
                    visited_rooms.add(key)
                    stack.append(key)
        return len(visited_rooms) == len(rooms)