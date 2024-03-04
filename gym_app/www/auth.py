import frappe
from frappe.sessions import Session, clear_sessions, delete_session, get_expiry_in_seconds

def logout(self, arg="", user=None):
		if not user:
			user = frappe.session.user
		self.run_trigger("on_logout")

		if user == frappe.session.user:
			delete_session(frappe.session.sid, user=user, reason="User Manually Logged Out")
			self.clear_cookies()
		else:
			clear_sessions(user)