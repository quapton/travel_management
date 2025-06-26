import frappe
from frappe.utils import cint, get_system_timezone
from frappe.sessions import get_csrf_token

no_cache = 1

def get_context(context):
	frappe.db.commit()

	context.boot = get_boot()
	context.template = "templates/web.html"  # Ensures Frappe layout loads
	context.title = "Travel Management"
	context.csrf_token = get_csrf_token()
	return context

def get_boot():
	return frappe._dict(
		{
			"frappe_version": frappe.__version__,
			"default_route": "/travel_management",
			"site_name": frappe.local.site,
			"read_only_mode": frappe.flags.read_only,
			"csrf_token": get_csrf_token(),
			"setup_complete": cint(frappe.get_system_settings("setup_complete")),
			"sysdefaults": frappe.defaults.get_defaults(),
			"is_demo_site": frappe.conf.get("is_demo_site"),
			"is_fc_site": frappe.conf.get("is_fc_site", False),
			"timezone": {
				"system": get_system_timezone(),
				"user": frappe.db.get_value("User", frappe.session.user, "time_zone")
				or get_system_timezone(),
			},
		}
	)
