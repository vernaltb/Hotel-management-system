from person import *
from staff import *
from hotel import *
from rooms import *

class Admin(Person):
    last_id = 1000
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)
        self.unique_id = "A" + str(Admin.last_id)
        Admin.last_id += 1

    def __str__(self):
        return f"{super().__str__()} ID: {self.unique_id}"
    
    def describe_admin(self):
        print(f"{self.unique_id}: {self.name} is an admin.")

    def create_staff_acc(self, staff_details):
        Staff(**staff_details)

    def remove_staff_member(self, staff_id):
        if staff_id in Staff.staffs:
            del Staff.staffs[staff_id]

    def update_staff_role(self, staff_id, new_role):
        if staff_id in Staff.staffs:
            Staff.staffs[staff_id].role = new_role

    def approve_maintenance_request(self, room_id, maintenance_type):
        for room in Rooms.maintenance_need:
            if room == room_id:
                Rooms.maintenance_need[room_id] = True
                print(f"Room {room_id} maintenance of type {maintenance_type} is approved.")
                
                

    def generate_payroll_report(self):
        maintenance = []
        receptionist = []
        houskeeping = []
        for staff in Staff.staffs.values():
            if staff.role ==  "Maintenance":
                maintenance.append(staff.salary)
            elif staff.role == "Receptionist":
                receptionist.append(staff.salary)
            elif staff.role == "Houskeeping":
                houskeeping.append(staff.salary)

        avg_maintenance = sum(maintenance) / len(maintenance)
        avg_receptionist = sum(receptionist) / len(receptionist)
        avg_houskeeping = sum(houskeeping) / len(houskeeping)

        print(f"Average salary of maintenance staff: {avg_maintenance},
        Average salary of receptionist staff: {avg_receptionist},
        Average salary of houskeeping staff: {avg_houskeeping}.")
            
