app_name = "cspa_assist"
app_title = "Cspa Assist"
app_publisher = "SARL MYNDALL"
app_description = "CS & PA Assist"
app_email = "contact@myndall.com"
app_license = "unlicense"
app_icon = "icon.png"   # or path to your own

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
	{
		"name": "cspa_assist",
		# "logo": "/assets/cspa_assist/logo.png",
		"title": "Cspa Assist",
		"route": "/cspa_assist",
		# "has_permission": "cspa_assist.api.permission.has_app_permission"
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cspa_assist/css/cspa_assist.css"
# app_include_js = "/assets/cspa_assist/js/cspa_assist.js"

# include js, css files in header of web template
# web_include_css = "/assets/cspa_assist/css/cspa_assist.css"
# web_include_js = "/assets/cspa_assist/js/cspa_assist.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cspa_assist/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "cspa_assist/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "app/cspa-assistance"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "cspa_assist.utils.jinja_methods",
# 	"filters": "cspa_assist.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "cspa_assist.install.before_install"
# after_install = "cspa_assist.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cspa_assist.uninstall.before_uninstall"
# after_uninstall = "cspa_assist.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "cspa_assist.utils.before_app_install"
# after_app_install = "cspa_assist.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "cspa_assist.utils.before_app_uninstall"
# after_app_uninstall = "cspa_assist.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cspa_assist.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cspa_assist.tasks.all"
# 	],
# 	"daily": [
# 		"cspa_assist.tasks.daily"
# 	],
# 	"hourly": [
# 		"cspa_assist.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cspa_assist.tasks.weekly"
# 	],
# 	"monthly": [
# 		"cspa_assist.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "cspa_assist.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cspa_assist.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cspa_assist.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["cspa_assist.utils.before_request"]
# after_request = ["cspa_assist.utils.after_request"]

# Job Events
# ----------
# before_job = ["cspa_assist.utils.before_job"]
# after_job = ["cspa_assist.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"cspa_assist.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

