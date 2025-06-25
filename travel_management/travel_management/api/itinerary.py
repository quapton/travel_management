import frappe
from frappe import _

@frappe.whitelist()
def get_user_itineraries(user=None):
    user = user or frappe.session.user
    return frappe.get_all("Itinerary", filters={"owner": user}, fields=["name", "title", "start_date", "end_date"])
