import datetime

class Rooms:
    all_rooms = {}
    cleaned_rooms = []
    maintenance_need = {}
    last_id = 100
    def __init__(self, room_type):
        self.room_id = "R" + str(Rooms.last_id)
        self.room_type = room_type
        self.room_status = False
        Rooms.all_rooms.update({self.room_id: self})
        Rooms.last_id += 1

    def __str__(self):
        return f"room id: {self.room_id}, type: {self.room_type}, status: {self.room_status}"
    
    def set_room_status(self, new_status):
        self.room_status = new_status

    def schedule_room_maintenance(self, maintenance_type):
        self.maintenance_type = maintenance_type
        date = input("Enter date (YYYY-MM-DD): ")
        self.maintenance_type_date = datetime.datetime.date.strptime(date, "%Y-%m-%d")
        Rooms.maintenance_need.update({self.room_id: False})

