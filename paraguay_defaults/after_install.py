import frappe

def after_install():
    add_fields_to_serie()

def add_fields_to_serie():
    frappe.db.sql("""alter table tabSeries add column creation datetime(6)""")
    frappe.db.sql("""alter table tabSeries add column modified datetime(6)""")
    frappe.db.sql("""alter table tabSeries add column owner varchar(140)""")
    frappe.db.sql("""alter table tabSeries add column modified_by varchar(140)""")
    frappe.db.sql("""alter table tabSeries add column docstatus int(1)""")
    frappe.db.sql("""alter table tabSeries add column idx int(8)""")
