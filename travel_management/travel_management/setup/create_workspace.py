import frappe
import json
import os

def execute():
    path = os.path.join(os.path.dirname(__file__), "travel_management_workspace.json")
    with open(path) as f:
        workspace = json.load(f)

    if not frappe.db.exists("Workspace", workspace["name"]):
        doc = frappe.get_doc(workspace)
        doc.insert(ignore_permissions=True)
        frappe.db.commit()
