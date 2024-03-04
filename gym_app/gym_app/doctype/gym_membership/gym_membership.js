// Copyright (c) 2024, Eshetie and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership", {
	setup(frm) {

	},

     validate: function(frm) {         
          let from = new Date(frm.doc.from);
          let to = new Date(frm.doc.to);
          let date = new Date(frappe.datetime.nowdate()) 

          let from_assert = from < date;

          let to_assert = to <= from;
          
          console.log(to_assert)

          if (from_assert) {
               frm.set_value('from', null);
			frm.refresh_field('from');
               frappe.msgprint('You cannot select a past date in From Date');
          } 
          
          if (to_assert) {
               frm.set_value('to', null);
			frm.refresh_field('to');
               frappe.msgprint('You cannot select a To date before/equal the From date');
          }       
     } 
});
