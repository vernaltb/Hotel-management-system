import json
from guests import *
from staff import *
from rooms import *

data = {
    "rooms" : Rooms.all_rooms,
    "guests" : Guest.guests,
    "staffs" : Staff.staffs
    }

with open("data.json", "x") as file:
    json.dump(data, file)