# Copyright (c) 2024, Eshetie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymClassSubscription(Document):
	def validate(self):
		self.set_status()  
          
	def set_status(self): 
		gym_class = frappe.get_doc("Gym Class", self.class_name)

		print(f'\n\n\n\n\n {gym_class.class_status} \n\n\n\n\n\n')

		if not gym_class: 
			frappe.throw("Gym Class does not exist")               
		
		else: 
			if gym_class.class_status == 'Available':
				gym_class.class_status = "On Request"
				gym_class.save()
			else:
				frappe.throw("Gym Class is not available")
		 

	@frappe.whitelist()
	def book_class(data):
		class_name = data.get('class_name')
		member = data.get('member')

		# Perform necessary operations with class_name and member

		frappe.msgprint(f"Booking class: {class_name} for member: {member}")