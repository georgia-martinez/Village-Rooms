import pandas as pd
import yaml
import csv

def sortable_room(room, priority, orderings):
    vals = []

    for p in priority:
        vals.append(orderings[p].index(getattr(room, p)))

    return tuple(vals)

class Room():
    def __init__(self, house, room, view, large):
        self.house = house
        self.room = room
        self.floor = int(str(self.room)[0])
        self.view = view
        self.large = large
    
    def __str__(self):
        return f"House {self.house} Room #{self.room} (view: {self.view}, large: {self.large})"

if __name__ == "__main__":
    
    # Read config
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    priority = config["priority"]

    orderings = dict()
    room_attrs = ["house", "view", "floor", "large"]

    for attr in room_attrs:
        orderings[attr] = config[attr]

    # Put all of the rooms in a list and sort by priority
    df = pd.read_csv(config["input"])

    all_rooms = []

    for index, row in df.iterrows():
        new_room = Room(row["house"], row["room"], row["view"], row["large"])
        all_rooms.append(new_room)

    all_rooms.sort(key=lambda room: sortable_room(room, priority, orderings))

    # Save ranking as csv
    with open(config["output"], 'w') as csvfile: 
        writer = csv.writer(csvfile) 
            
        header = ["house", "room", "view", "large"]
        writer.writerow(header)

        for room in all_rooms:
            room_dict = vars(room)

            row = [room_dict[attr] for attr in header]
            writer.writerow(row)

            print(room)