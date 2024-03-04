

function book_class(event, class_name){
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

function test(){
     console.log('Hello there');
     $.ajax({
          url: "/api/method/gym_app.home.book_class",
          type: "POST",
          data: {
              doctype_name: "Gym Member"
          },
          success: function(response) {
              $("#result").text(response.message);
          },
          error: function(xhr, status, error) {
              console.error(error);
          }
      });
}