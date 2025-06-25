from frappe import _

def get_data():
    return {
        "fieldname": "travel_management",
        "transactions": [
            {"label": _("Planning"), "items": ["Itinerary", "Traveler"]},
            {"label": _("Transport"), "items": ["Bus Trip"]},
            {"label": _("Stay"), "items": ["Hotel Room"]}
        ]
    }
