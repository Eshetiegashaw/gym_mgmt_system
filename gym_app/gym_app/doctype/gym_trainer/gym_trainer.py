# Copyright (c) 2024, Eshetie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymTrainer(Document):
	def validate(self):
		self.set_full_name()
		if not self.email:
			self.email = self.first_name + '' + '@gym.com'

	def set_full_name(self):
		self.full_name = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))
	
	def before_save(self):
		self.user = self.create_user()  


	def create_user(self):
		if not frappe.db.exists("User", self.email):
			user = frappe.get_doc(
				dict(
					doctype="User",
                         email=self.email,
                         mobile_no=self.phone,
                         first_name=self.first_name,
                         middle_name=self.middle_name,
                         last_name=self.last_name,
                         new_password='@gym_trainer',
                         roles=[{"role": "Gym Trainer"}],
				)
			)

			user.flags.ignore_permissions = True
			user.insert()
			return user.name

		else:
			frappe.throw("User already exists, please provide unique email and check again")
			return None