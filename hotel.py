from guests import Guest
from rooms import *


class Hotel:
    available_rooms = {}

    @staticmethod
    def list_available_rooms(self, room_type):
        print("Available rooms of this type:")
        for rid, rtype in Hotel.available_rooms.items():
            if rtype == room_type:
                print(rid)


    def get_guest_detailes(guest_id):
        if guest_id in Guest.guests:
            print(Guest.guests[guest_id])
    @staticmethod
    def add_rooms():
        for room in Rooms.all_rooms:
            if room.room_status == True:
                Hotel.available_rooms.update({room.room_id : room, room.room_type : room.room_type})
           
    

    def summerize_daily_operations(self):
        pass
