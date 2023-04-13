import pandas as pd
import yaml

def sortable_room(room, priority, orderings):
    vals = []

    for p in priority:
        vals.append(orderings[p].index(getattr(room, p)))

    return tuple(vals)

class Room():
    def __init__(self, house, room, view, large):
        self.house = house
        self.room_num = room
        self.floor = int(str(self.room_num)[0])
        self.view = view
        self.large = large
    
    def __str__(self):
        return f"House {self.house} Room #{self.room_num} (view: {self.view}, large: {self.large})"

if __name__ == "__main__":
    # Read csv with the rooms
    ROOMS_PATH = "rooms.csv"
    df = pd.read_csv(ROOMS_PATH)

    # Put all of the rooms in a list
    all_rooms = []

    for index, row in df.iterrows():
        new_room = Room(row["House"], row["Room Number"], row["View"], row["Large"])
        all_rooms.append(new_room)

    # Read config
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Sort by priority
    priority = config["priority"]

    orderings = {
        "house": config["house"],
        "view": config["view"],
        "floor": config["floor"],
        "large": [True, False]
    }

    all_rooms.sort(key=lambda room: sortable_room(room, priority, orderings))

    for room in all_rooms:
        print(room)