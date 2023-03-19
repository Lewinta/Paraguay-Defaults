# Copyright (c) 2022, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

from paraguay_defaults.client import validate_access
from frappe.model.naming import make_autoname

scope = "Print Format: Sales Invoice"

def autoname(doc, method):
	doc.name = make_autoname(make_name(doc))

def make_name(doc):
	if not doc.cost_center:
		frappe.throw("""Favor seleccionar un centro de costos para crear esta factura""")

	cc = frappe.get_value("Cost Center", doc.cost_center, ["punto_de_expedicion", "parent_cost_center"], as_dict=True)
	sucursal = frappe.get_value("Cost Center", cc.parent_cost_center, "cost_center_number", as_dict=True)
	if not sucursal.cost_center_number:
		frappe.throw(f"Favor colocar un numero de centro de costos para {cc.parent_cost_center}")

	if not cc.punto_de_expedicion:
		frappe.throw(f"Favor colocar el punto de expedicion en el centro de costos {doc.cost_center}")
	
	suc = sucursal.cost_center_number.zfill(3)
	exp = cc.punto_de_expedicion.zfill(3)
	return f"{suc}-{exp}-.#######"
	
def validate(doc, method=None, settings=None):
	set_timbrado(doc)

def set_timbrado(doc):
	if not doc.cost_center:
		frappe.throw("No es posible generar facturas sin el centro de costos")

	result = frappe.db.sql("""
		select 
			timbrado,
			valido_desde,
			valido_hasta
		from 
			`tabTimbrado por Sucursal` 
		where
			parent = 'Configuracion Regional'
		and 
			sucursal = %s""", doc.cost_center, as_dict=True)
	if not result:
		frappe.throw("""Favor agregar el centro de costos en la <b><a href="/app/configuracion-regional/Configuracion%20Regional">Configuracion Regional</a></b>""")
	result = result[0]
	doc.update({
		"timbrado": result.timbrado,
		"valido_desde": result.valido_desde,
		"valido_hasta": result.valido_hasta,
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
