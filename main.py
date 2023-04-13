import pandas as pd
import yaml
from dataclasses import dataclass

@dataclass
class Room():
    house: int
    room_num: int
    view: str
    large: bool

    @property
    def floor(self) -> int:
        floor = int(str(self.room_num)[0])
        return floor
    
    def __str__(self):
        return f"House {self.house} Room #{self.room_num} (view: {self.view}, large: {self.large})"

# Read csv with the rooms
ROOMS_PATH = "rooms.csv"
df = pd.read_csv(ROOMS_PATH)

# Put all of the rooms in a list
all_rooms = []

for index, row in df.iterrows():
    new_room = Room(row["House"], row["Room Number"], row["View"], row["Large"])
    all_rooms.append(new_room)

# Read config with the priority ordering
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

house = config["house"]
view = config["view"]
floor = config["floor"]

# Sort the rooms
all_rooms.sort(key=lambda r: (-r.large, view.index(r.view), house.index(r.house), floor.index(r.floor)))

for room in all_rooms:
    print(room)
