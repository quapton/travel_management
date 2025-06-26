
import frappe

def generate_bus_seats(bus_doc):
    rows = ['A', 'B', 'C', 'D']
    for i in range(1, 11):  # 10 seats per row = 40 seats
        for row in rows:
            seat_num = f"{row}{i}"
            bus_doc.append("seat_map", {
                "seat_number": seat_num,
                "is_booked": 0
            })

def assign_travelers_to_bus_and_rooms(trip_doc):
    travelers = trip_doc.get("travelers") or []
    if len(travelers) > trip_doc.total_seats:
        frappe.throw("Not enough bus seats for all travelers.")

    # Bus seat assignment
    seats = frappe.get_all("Bus Seat",
        filters={"parent": trip_doc.bus, "is_booked": 0},
        limit=len(travelers)
    )
    for i, seat in enumerate(seats):
        frappe.db.set_value("Bus Seat", seat.name, {
            "is_booked": 1,
            "traveler": travelers[i].traveler
        })

    # Room allocation
    if trip_doc.room_type == "Shared":
        rooms = frappe.get_all("Room", filters={"is_shared": 1})
        for traveler_row in travelers:
            traveler = traveler_row.traveler
            gender = frappe.get_value("Customer", traveler, "gender")
            assigned = False

            for r in rooms:
                room = frappe.get_doc("Room", r.name)
                if len(room.room_members) < room.capacity:
                    if all(m.gender == gender for m in room.room_members):
                        room.append("room_members", {
                            "traveler": traveler,
                            "gender": gender,
                            "assigned_on": frappe.utils.today()
                        })
                        room.save()
                        assigned = True
                        break

            if not assigned:
                frappe.msgprint(f"No suitable room found for {traveler}")
