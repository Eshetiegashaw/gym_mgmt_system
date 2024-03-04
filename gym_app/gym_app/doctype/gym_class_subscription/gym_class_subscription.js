// Copyright (c) 2024, Eshetie and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Class Subscription", {
	refresh(frm) {

	},
});


function book_class(class_name){
     var member = event.target.getAttribute('data-member');
     console.log('Hello there');
     console.log('Class Name: ' + class_name);
     console.log('Member: ' + member); 
     frappe.call({
          method: 'gym_app.gym_app.doctype.gym_class_subscription.book_class', 
          args: {
               'class_name': class_name,  // Pass class_name to backend
               'member': member  // Pass member to backend
          },
          callback: function(r) {
               if (!r.exc) {
                    // code snippet
               }
          }
     });
}
