# Copyright (c) 2024, Eshetie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries

class GymClass(Document):
	def validate(self):
		self.class_name = self.class_name.capitalize()
		# self.autoname() 
		self.total_class()
		self.added_class()
		# self.class_validate()

	def autoname(self):
		classes = frappe.get_all("Gym Class", order_by="creation")
		 
		if len(classes) > 0:
			name = str(classes[-1].name.split("-")[-1]) 
			
			# increment sequence number and re-format name
			seq_no = int(name.split("-")[-1]) + 1  			
			self.name = f"Class-{self.class_name}-{seq_no:003d}"
		else: 
			self.name = f"Class-{self.class_name}-001"

	def total_class(self):
		total_classes = 0;
		# get the total number of classes
		classes = frappe.db.sql(f"""SELECT value FROM `tabSingles` WHERE doctype = 'Gym Setting' AND field = 'number_of_classes';""", as_dict=True)
		if classes:
			total_classes = classes[0].value; 

		self.total_classes = int(total_classes)
	
	def added_class(self):
		# getting the total number of classes added before
		added_classes = frappe.get_all('Gym Class')
		self.added =  len(added_classes)
	
	def class_validate(self):
		if not self.added < self.total_classes:
			frappe.throw("We haven't any available class to be added. All classes are added.")
		
