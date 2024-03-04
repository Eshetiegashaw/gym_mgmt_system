# Copyright (c) 2024, Eshetie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymLocker(Document):
	def validate(self):
		self.locker_name = self.locker_name.upper()  
		self.autoname()
		self.total_locker()
		self.added_locker()
		self.locker_validate()

	def autoname(self):
		lockers = frappe.get_all("Gym Locker", order_by="creation")
		 
		if len(lockers) > 0:
			name = str(lockers[-1].name.split("-")[-1]) 
			
			# increment sequence number and re-format name
			seq_no = int(name.split("-")[-1]) + 1  			
			self.name = f"Locker-{self.locker_name}-{seq_no:003d}"
		else: 
			self.name = f"Locker-{self.locker_name}-001"

	def total_locker(self):
		total_lockers = 0;
		# get the total number of lockers
		lockers = frappe.db.sql(f"""SELECT value FROM `tabSingles` WHERE doctype = 'Gym Setting' AND field = 'number_of_lockers';""", as_dict=True)
		if lockers:
			total_lockers = lockers[0].value; 

		self.total_lockers = int(total_lockers)
	
	def added_locker(self):
		# getting the total number of lockers added before
		added_lockers = frappe.get_all('Gym Locker')
		self.added =  len(added_lockers)
	
	def locker_validate(self):
		if not self.added < self.total_lockers:
			frappe.throw("We haven't any available locker to be added. All lockers are added.")
