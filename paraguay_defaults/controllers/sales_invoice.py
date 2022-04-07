# Copyright (c) 2022, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

from paraguay_defaults.client import validate_access


scope = "Print Format: Sales Invoice"


def validate(doc, method=None, settings=None):
	conf =  frappe.db.get_singles_dict("Configuracion Regional")
	doc.update({
		"timbrado": conf.timbrado,
		"valido_desde": conf.valido_desde,
		"valido_hasta": conf.valido_hasta,
	})

def before_print(doc, method=None, settings=None):
	if validate_access(scope):
		doc.html_template = get_html_template(doc)
	else:
		doc.html_template = get_alternate_template(doc)


def get_html_template(doc):
	# your template goes here...
	template = "templates/punto_de_venta.html"

	context = {
		"doc": doc.as_dict(),
		"frappe.utils": frappe.utils,
	}

	return frappe.render_template(template, context)


def get_alternate_template(doc):
	return """
		<h1 style="text-align: center;">
			Formato de Impresión no permitido.
		</h1>
	"""
