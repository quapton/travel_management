import frappe
from frappe.model.document import Document

class Trip(Document):
    def validate(self):
        self.available_seats = self.total_seats - len(self.get("days", []))

    def on_submit(self):
        # Bus Seat Assignment
        seats = frappe.get_all("Bus Seat",
            filters={"parent": self.bus, "is_booked": 0},
            limit=self.total_seats)
        travelers = self.get("travelers") or []
        for i, seat in enumerate(seats):
            if i < len(travelers):
                frappe.db.set_value("Bus Seat", seat.name, "is_booked", 1)
                frappe.db.set_value("Bus Seat", seat.name, "traveler", travelers[i].traveler)

        # Room Allocation for shared rooms
        if self.room_type == "Shared":
            rooms = frappe.get_all("Room", filters={"is_shared": 1})
            for traveler in travelers:
                # Example: assign to first available room based on capacity
                for r in rooms:
                    room = frappe.get_doc("Room", r.name)
                    if len(room.room_members) < room.capacity:
                        room.append("room_members", {
                            "traveler": traveler.traveler,
                            "gender": frappe.get_value("Customer", traveler.traveler, "gender"),
                            "assigned_on": frappe.utils.today()
                        })
                        room.save()
                        break
