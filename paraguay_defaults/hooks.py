from . import __version__ as app_version

app_name = "paraguay_defaults"
app_title = "Paraguay Defaults"
app_publisher = "Lewin Villar"
app_description = "A custom app to manage paraguay custom settings"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "lewinvillar@tzcode.tech"
app_license = "GPT3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/paraguay_defaults/css/paraguay_defaults.css"
# app_include_js = "/assets/paraguay_defaults/js/paraguay_defaults.js"

# include js, css files in header of web template
# web_include_css = "/assets/paraguay_defaults/css/paraguay_defaults.css"
# web_include_js = "/assets/paraguay_defaults/js/paraguay_defaults.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "paraguay_defaults/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "paraguay_defaults.install.before_install"
# after_install = "paraguay_defaults.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "paraguay_defaults.uninstall.before_uninstall"
# after_uninstall = "paraguay_defaults.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "paraguay_defaults.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"before_print": "paraguay_defaults.controllers.sales_invoice.before_print",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"paraguay_defaults.tasks.all"
# 	],
# 	"daily": [
# 		"paraguay_defaults.tasks.daily"
# 	],
# 	"hourly": [
# 		"paraguay_defaults.tasks.hourly"
# 	],
# 	"weekly": [
# 		"paraguay_defaults.tasks.weekly"
# 	]
# 	"monthly": [
# 		"paraguay_defaults.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "paraguay_defaults.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "paraguay_defaults.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "paraguay_defaults.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"paraguay_defaults.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
