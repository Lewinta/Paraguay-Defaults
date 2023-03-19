import frappe
from frappe import clear_cache

@frappe.whitelist()
def impersonate(user):
    if "System Manager" in frappe.get_roles():
        clear_cache()
        frappe.local.login_manager.login_as(user)
        return "Impersonated as: {0}".format(str(user))
