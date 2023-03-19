# Copyright (c) 2022, Lewin Villar and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import cstr

def execute(filters=None):
	return get_columns(filters), get_data(filters)

def get_columns(filters):	
	if filters.get("view_details"):
		columns = (
			(_("Sales Invoice"), "Link/Sales Invoice", 150),
			(_("Date"), "Date", 100),
			(_("Customer"),  "Data", 220),
			(_("Sales Partner"),  "Data", 220),
			(_("Item"),  "Data", 220),
			(_("Amount"),  "Currency", 120),
			(_("Percentage"), "Percent", 120),
			(_("Commission"), "Currency", 120),
		)
	else:
		columns = (
			(_("Sales Partner"),  "Data", 220),
			(_("Amount"),  "Currency", 120),
			(_("Commission"), "Currency", 120),
		)
	formatted_columns = []

	for label, fieldtype, width in columns:
		formatted_columns.append(
			get_formatted_column(_(label), fieldtype, width)
		)

	return formatted_columns

def get_fields(filters):
	"""
		Return sql fields ready to be used on a query
	"""
	if filters.get("view_details"):
		fields = (
			("Sales Invoice", "name"),
			("Sales Invoice", "posting_date"),
			("Sales Invoice", "customer"),
			("Sales Partner", "name"),
			("CONCAT('<b>',`tabSales Invoice Item`.item_code, '</b>:',`tabSales Invoice Item`.item_name )"),
			("Sales Invoice Item", "amount"),
			("Commissions by Item Group", "percentage"),
			("`tabSales Invoice Item`.amount * `tabCommissions by Item Group`.percentage / 100.0"),
		)
	else:
		fields = (
			("Sales Partner", "name"),
			("SUM(`tabSales Invoice Item`.amount) as amount"),
			("SUM(`tabSales Invoice Item`.amount * `tabCommissions by Item Group`.percentage / 100.0) as commission"),
		)
	sql_fields = []

	for args in fields:
		sql_field = get_field(args)
		sql_fields.append(sql_field)

	return ", ".join(sql_fields)
	
def get_data(filters):
	fields = get_fields(filters)
	conditions = get_conditions(filters)
	extra_conditions = '' if filters.get("view_details") else "GROUP BY \n\t\t\t`tabSales Invoice`.sales_partner"
	return frappe.db.sql("""
		SELECT
			{fields}
		FROM
			`tabSales Invoice`
		JOIN
			`tabSales Invoice Item`
		ON
			`tabSales Invoice`.name = `tabSales Invoice Item`.parent
		JOIN
			`tabItem`
		ON
			`tabItem`.item_code = `tabSales Invoice Item`.item_code
		JOIN
			`tabSales Partner`
		ON
			`tabSales Invoice`.sales_partner = 	`tabSales Partner`.name
		JOIN
			`tabCommissions by Item Group`
		ON
			`tabCommissions by Item Group`.parent = `tabSales Partner`.name
		AND
			`tabItem`.item_group = `tabCommissions by Item Group`.item_group
		WHERE
			{conditions}
		{extra_conditions}
		

		""".format(fields=fields, conditions=conditions or "1 = 1", extra_conditions=extra_conditions),
            filters, debug=True)

def get_conditions(filters):
	conditions = [
		("Sales Invoice", "docstatus", "=", 1)
	]
	if filters.get('sales_partner'):
			conditions.append(
				("Sales Invoice", "sales_partner", "=", "%(sales_partner)s")
			)
	sql_conditions = []

	for doctype, fieldname, compare, value in conditions:
		sql_condition = "`tab{doctype}`.`{fieldname}` {compare} {value}\n" \
				.format(doctype=doctype, fieldname=fieldname, compare=compare,
						value=value)
						
		sql_conditions.append(sql_condition)

	return " And ".join(sql_conditions)

def get_field(args):
	if len(args) == 2:
		doctype, fieldname = args
	else:
		return args if isinstance(args, str) \
			else " ".join(args)

	sql_field = "`tab{doctype}`.`{fieldname}`" \
		.format(doctype=doctype, fieldname=fieldname)

	return sql_field

def get_formatted_column(label, fieldtype, width):
	# [label]:[fieldtype/Options]:width
	parts = (
		_(label),
		fieldtype,
		cstr(width)
	)
	return ":".join(parts)
