# Copyright (c) 2023, Lewin Villar and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.query_builder import DocType, Criterion
def execute(filters=None):
	return get_columns(), get_data(filters)

def get_columns():
	return [
		{
			"label": _("Item Code"),
			"fieldname": "item_code",
			"fieldtype": "Data",
			"width": 300
		},
		{
			"label": _("Item Name"),
			"fieldname": "item_name",
			"fieldtype": "Data",
			"width": 500
		},
		{
			"label": _("Price List"),
			"fieldname": "price_list",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Price List Rate"),
			"fieldname": "price_list_rate",
			"fieldtype": "Currency",
			"width": 200
		},
	]

def get_conditions(filters):
	return conditions

def get_data(filters):
	conditions = []
	ItemPrice = frappe.qb.DocType("Item Price")
	
	if filters.get("item_code"):
		conditions.append(ItemPrice.item_code == filters.get("item_code"))
	if filters.get("price_list"):
		conditions.append(ItemPrice.price_list == filters.get("price_list"))
	if filters.get("selling"):
		conditions.append(ItemPrice.selling == filters.get("selling"))
	if filters.get("buying"):
		conditions.append(ItemPrice.buying == filters.get("buying"))
	
	return frappe.qb.from_(ItemPrice).select(
		ItemPrice.item_code,
		ItemPrice.item_name,
		ItemPrice.price_list,
		ItemPrice.price_list_rate
	).where(
		Criterion.all(conditions)
	).orderby(
		ItemPrice.item_name
	).run(as_dict=True)