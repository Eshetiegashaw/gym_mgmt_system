import frappe 
# from frappe.model.document import Document


# class GymLocker(Document):

def get_context(context):
     context.user = frappe.session.user
     context.is_autheticate = False

     print(f'\n\n\n\n\n {context.user} \n\n\n\n\n\n')

     if context.user != "Guest":
          context.is_authenticate = True
     else:
          context.is_authenticate = False 

     get_members(context)

def get_members(context):
     context.cur_trainer = frappe.db.get_value("Gym Trainer", {"email": context.user}, "name")
     context.members = frappe.db.sql(f"""SELECT * FROM `tabGym Trainer Subscription` st_sub JOIN `tabGym Trainer` trainer ON st_sub.trainer = trainer.name JOIN `tabGym Member` mem ON st_sub.member = mem.name WHERE st_sub.trainer = '{context.cur_trainer}';""", as_dict=True)
     return context
