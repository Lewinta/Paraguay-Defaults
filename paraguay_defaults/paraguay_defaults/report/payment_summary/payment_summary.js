// Copyright (c) 2022, Lewin Villar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Payment Summary"] = {
	"filters": [
		{
			"label": __("From Date"),
			"fieldname": "from_date",
			"fieldtype": "Date",
			"default": frappe.datetime.nowdate()
		},
		{
			"label": __("To Date"),
			"fieldname": "to_date",
			"fieldtype": "Date",
			"default": frappe.datetime.nowdate()
		},
		{
			"label": __("User"),
			"fieldname": "user",
			"fieldtype": "Link",
			"options": "User",
			"default": frappe.session.user,
			"read_only": !frappe.user.has_role("System Manager"),
		},
		{
			"label": __("Summary"),
			"fieldname": "summary",
			"fieldtype": "Check",
			"default": 1,
		}
	]
};
