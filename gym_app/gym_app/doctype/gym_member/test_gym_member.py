# Copyright (c) 2024, Eshetie and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymMember(FrappeTestCase):
	def test_fullname(self):
		gym_member = frappe.get_doc({
			"doctype":"Gym Member",
			"first_name":"Eshetie",
			"middle_name":"Gashaw",
			"last_name": "Yigizaw",
			"phone": "+215-965578302"
		}).insert()
		
		self.assertEqual(gym_member.full_name, "Eshetie Gashaw Yigizaw")
