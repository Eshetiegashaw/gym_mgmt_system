import frappe
from frappe.sessions import Session, clear_sessions, delete_session, get_expiry_in_seconds


def get_context(context): 
     context.user = frappe.session.user
     context.is_authenticate = False  


     print(f'\n\n\n\n\n  authentication {context.is_authenticate} \n\n\n\n\n\n')

     if context.user:
          context.is_authenticate = True
     else:
          context.is_authenticate = False  

     return context

def logout(self, arg="", user=None):
		if not user:
			user = frappe.session.user
		self.run_trigger("on_logout")

		if user == frappe.session.user:
			delete_session(frappe.session.sid, user=user, reason="User Manually Logged Out")
			self.clear_cookies()
		else:
			clear_sessions(user)