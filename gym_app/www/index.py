# Copyright (c) 2024, Eshetie and contributors
# For license information, please see license.txt

import frappe

def get_context(context):
    redirect_to = frappe.local.request.args.get("redirect-to")
    context.user = frappe.session.user
    context.is_authenticate = False 

    if context.user != "Guest":
          context.user_role = frappe.get_roles(context.user) 
          
          if not redirect_to:
               if "Gym Member" in context.user_role:
                    redirect_to = "/members/home"  
               elif "Gym Trainer" in context.user_role:
                    redirect_to = "/trainers/home"  
               else:
                    redirect_to = "/login#login"

          if redirect_to != "login":
               frappe.local.flags.redirect_location = redirect_to
               raise frappe.Redirect

    print(f'\n\n\n\n\n {context.user}  authentication {context.is_authenticate} \n\n\n\n\n\n')

    if context.user != "Guest":
          context.is_authenticate = True
    else:
          context.is_authenticate = False  


    return context



        
        