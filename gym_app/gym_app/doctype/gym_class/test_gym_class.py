# Copyright (c) 2024, Eshetie and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymClass(FrappeTestCase):
	def test_class(self):
		gym_member = frappe.get_doc({
			"doctype":"Gym Class",
			"member":"Ahmed",
			"class_status": "Available",
			"price": 430 
		}).insert()
		
		self.assertEqual(gym_member.member, "Ahmed")
