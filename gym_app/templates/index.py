import frappe

def get_context(context):
     context.user = frappe.session.user
     context.is_autheticate = context.user != "Guest"

     return context