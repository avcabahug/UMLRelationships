# Composition (Strong Has-a)

class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        # House creates and owns the rooms
        self.rooms = [Room("Kitchen"), Room("Bedroom")]

# Run
my_house = House()
for room in my_house.rooms:
    print("Room:", room.name)
