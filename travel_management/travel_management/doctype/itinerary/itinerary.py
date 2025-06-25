import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import nowdate

@frappe.whitelist()
def get_user_itineraries(user=None):
    """Get all itineraries created by a user (defaults to current user)"""
    user = user or frappe.session.user
    itineraries = frappe.get_all("Itinerary", filters={"owner": user}, fields=["name", "title", "start_date", "end_date"])
    return itineraries

@frappe.whitelist()
def create_itinerary(title, start_date, end_date, traveler):
    """Create a new itinerary document"""
    doc = frappe.new_doc("Itinerary")
    doc.title = title
    doc.start_date = start_date
    doc.end_date = end_date
    doc.traveler = traveler
    doc.insert()
    frappe.db.commit()
    return doc

@frappe.whitelist()
def delete_itinerary(name):
    """Delete an itinerary by name (ID)"""
    frappe.delete_doc("Itinerary", name)
    return {"message": "Itinerary deleted"}
