import frappe
from frappe.model.document import Document

class Itinerary(Document):
    def validate(self):
        if self.start_date > self.end_date:
            frappe.throw("End Date must be after Start Date")
