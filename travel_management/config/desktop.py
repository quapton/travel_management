from frappe import _

def get_data():
    return [
        {
            "module_name": "Travel Management",
            "type": "module",
            "label": _("Travel Management"),
            "color": "#1abc9c",
            "icon": "octicon octicon-globe",
            "link": "modules/Travel Management",
            "onboard": 1,
        }
    ]
