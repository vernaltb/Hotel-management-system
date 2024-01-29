from person import *
from rooms import *
from guests import *

class Staff(Person):
    staffs = {}
    last_id = 1000
    def __init__(self, name, contact_info, role):
        super().__init__(name, contact_info)
        self.unique_id = "S" + str(Staff.last_id)
        self.role = role
        Staff.staffs.update({self.unique_id: self})
        Staff.last_id += 1

    def __str__(self):
        return f"{super().__init__()}, ID: {self.unique_id}"

    def describe_staff(self):
        print(f"{self.unique_id}: {self.name} is a staff member.")

    def book_guest(self, guest_id, room_id):
        if self.role == "Receptionist":
            pass

    def check_out_guest(self, guest_id, room_id):
        if self.role == "Receptionist":
            if guest_id in Guest.guests:
                if room_id in guest_id.bookings["room_id"]: #guest_id.bookings????
                    print(f"Guest {guest_id} has checked out of room {room_id}.")
                else:
                    print(f"Guest {guest_id} is not booked in room {room_id}.")

    
    def mark_room_cleaned(self, room_id):
        if self.role == "Houskeeping":
            if room_id not in Rooms.cleaned_rooms:
                Rooms.cleaned_rooms.append(room_id)
                print(f"Room {room_id} has been cleaned.")
            else:
                print(f"Room {room_id} has already been cleaned.")
        else:
            print("You are not authorized to perform this action.")

    def request_cleaning_sup(self, requests):
        if self.role == "Houskeeping":
            self.requests = requests
        else:
            print("You are not authorized to perform this action.")

    def order_repair_material(self, material_list):
        if self.role == "Maintenance":
            self.material_list = material_list
        else:
            print("You are not authorized to perform this action.")

    def report_repair_done(self, room_id):
        if self.role == "Maintenance":
            for rid, status in Rooms.maintenance_need.items():
                if room_id == rid and status == True:
                    Rooms.maintenance_need.pop(rid)
                    print(f"Room {rid} is now repaired.")
                else:
                    print("you entered an invalid room id or the maintenanace request has not been approved yet.")
        else:
            print("You are not authorized to perform this action.")
