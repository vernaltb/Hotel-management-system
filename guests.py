from person import *
from rooms import *
from hotel import *

class Guest(Person):
    last_id_g = 100
    last_id_b = 100
    guests = {}
    def __init__(self, name, contact_info, unique_id):
        super().__init__(name, contact_info, unique_id)
        self.bookings = {}
        Guest.guests.update({self.unique_id : self})


    def __str__(self):
        return super().__str__()
    
    def describe_person(self):
        print(f"{self.name} is a guest.")

    def request_room_booking(self, room_types, dates):
        for room in Rooms.all_rooms:
            if room.room_type == room_types and room.room_status == True:
                room.set_room_status(False)
                Hotel.available_rooms.pop(room.room_id)
                booking_id = "R" + str(Guest.last_id_b)
                self.bookings.update({booking_id : {"room_id" : room.room_id, "dates" : dates}})
            break

    def amend_booking(self, booking_id, new_dates):
        if booking_id in self.bookings:
            self.bookings[booking_id]["dates"] = new_dates
    def cancel_booking(self, booking_id):
        if booking_id in self.bookings:
            self.bookings.pop(booking_id)

    def give_feedback(self, feedback_text):
        feedback = f"user {self.name} feedback: {feedback_text}"
        with open("feedbacks.txt", "x") as file:
            file.write(feedback + "\n")
