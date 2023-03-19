# Copyright (c) 2022, Lewin Villar and contributors
# For license information, please see license.txt

import frappe

from frappe import _
from pypika import CustomFunction, Criterion, Query, Field, functions as fn


def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data

def get_columns(filters):
	if filters.get("summary"):
		return [
			{
				"label": _("User"),
				"fieldname": "full_name",
				"fieldtype": "Data",
				"width": 180,
			},
			{
				"label": _("Mode of Payment"),
				"fieldname": "mode_of_payment",
				"fieldtype": "Data",
				"width": 180,
			},
			{
				"label": _("Total"),
				"fieldname": "total",
				"fieldtype": "Currency",
				"width": 180,
			}
		]
	else:
		return [
			{
				"label": _("User"),
				"fieldname": "full_name",
				"fieldtype": "Data",
				"width": 180,
			},
			{
				"label": _("Mode of Payment"),
				"fieldname": "mode_of_payment",
				"fieldtype": "Data",
				"width": 180,
			},
			{
				"label": _("Document"),
				"fieldname": "document",
				"fieldtype": "Data",
				"width": 180,
			},
			{
				"label": _("Total"),
				"fieldname": "total",
				"fieldtype": "Currency",
				"width": 180,
			}
		]

def get_data(filters):
	Invoice = frappe.qb.DocType('Sales Invoice')
	InvoicePayment = frappe.qb.DocType('Sales Invoice Payment')
	User = frappe.qb.DocType('User')
	Payment = frappe.qb.DocType('Payment Entry')
	
	invoice_conditions  = [ Invoice.docstatus == 1 ]
	payments_conditions = [ Payment.docstatus == 1 ,  Payment.payment_type == 'Receive']

	if filters.get("from_date"):
		invoice_conditions.append(Invoice.posting_date >= filters.get("from_date"))
		payments_conditions.append(Payment.posting_date >= filters.get("from_date"))

	if filters.get("to_date"):
		invoice_conditions.append(Invoice.posting_date <= filters.get("to_date"))
		payments_conditions.append(Payment.posting_date <= filters.get("to_date"))

	if filters.get("user"):
		invoice_conditions.append(Invoice.owner == filters.get("user"))
		payments_conditions.append(Payment.owner == filters.get("user"))

	payment_entries =  Query.from_(Payment).join(User).on(
		Payment.owner == User.name
	).select(
		User.name,
		User.full_name,
		Payment.name.as_('document'),
		Payment.mode_of_payment,
		Payment.paid_amount.as_('total'),
	).where(
		Criterion.all(payments_conditions)
	)
	
	pos_payments = Query.from_(InvoicePayment).inner_join(Invoice).on(
		InvoicePayment.parent == Invoice.name
	).inner_join(User).on(
		User.name == Invoice.owner
	).select(
		User.name,
		User.full_name,
		InvoicePayment.parent.as_('document'),
		InvoicePayment.mode_of_payment,
		InvoicePayment.base_amount.as_('total'),
	).where(
		Criterion.all(invoice_conditions)
	)

	if (filters.get('summary')):
		return frappe.qb.from_( pos_payments + payment_entries).select(
			Field('full_name'),
			Field('mode_of_payment'),
			fn.Sum(Field('total')).as_('total')
		).groupby(
			Field('name'),
			Field('mode_of_payment')
		).run()
	else:
		return frappe.qb.from_( pos_payments + payment_entries).select(
			Field('full_name'),
			Field('mode_of_payment'),
			Field('document'),
			Field('total')
		).run()


	