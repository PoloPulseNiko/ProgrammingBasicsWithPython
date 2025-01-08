floors = int(input())
rooms_per_floor = int(input())

for floor in range(floors, 0, -1):
    floor_rooms = []
    for room in range(rooms_per_floor):
        if floor == floors:
            floor_rooms.append(f"L{floor}{room}")
        elif floor % 2 == 0:
            floor_rooms.append(f"O{floor}{room}")
        else:
            floor_rooms.append(f"A{floor}{room}")
    print(" ".join(floor_rooms))