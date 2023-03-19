// Copyright (c) 2023, Lewin Villar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Consulta de Precios"] = {
	"filters": [
		{
			"fieldname":"item_code",
			"label": __("Item Code"),
			"fieldtype": "Link",
			"options": "Item",
		},
		{
			"fieldname":"price_list",
			"label": __("Price List"),
			"fieldtype": "Link",
			"options": "Price List",
		},
		{
			"fieldname":"selling",
			"label": __("Selling"),
			"fieldtype": "Check",
			"default": 1,
		},
		{
			"fieldname":"buying",
			"label": __("Buying"),
			"fieldtype": "Check",
			"default": 0,
		},
	]
};
