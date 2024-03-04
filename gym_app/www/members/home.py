import frappe 
from frappe.model.document import Document
 

def get_context(context): 
     context.user = frappe.session.user
     context.is_autheticate = False 

     # get the current member
     context.member = frappe.db.get_value("Gym Member", {"email": context.user}, "name")

     if context.user != "Guest":
          context.is_authenticate = True
     else:
          context.is_authenticate = False   

     get_membership(context)
     get_classes(context)
     get_lockers(context)
     get_trainers(context)
     get_workout_plan(context)  
     get_my_class(context)
     get_my_locker(context)
     get_my_trainer(context)
     get_my_workout(context)
     


    
# getting the classes nlist 
def get_classes(context):
     context.gym_classes = frappe.db.sql(f"""SELECT * FROM `tabGym Class`;""", as_dict = True)

# getting the lockers list and their status
def get_lockers(context):
     context.gym_lockers = frappe.db.sql(f"""SELECT name, locker_name, locker_status FROM `tabGym Locker`;""", as_dict = True)


# see the workout plan execrise plan and book foir them
def get_workout_plan(context):
     context.gym_workouts = frappe.db.sql(f"""SELECT name, exercise_name, exercise_duration FROM  `tabGym Workout Plan Exercise`;""", as_dict=True)


# See the trainers information and subecribe for them
def get_trainers(context):
     context.gym_trainers = frappe.db.sql(f"""SELECT name, full_name, specialization FROM `tabGym Trainer`;""", as_dict = True)

# see their classes
def get_my_class(context):      
     context.my_class = frappe.db.sql(f"""SELECT class_name, duration FROM `tabGym Class Subscription` sub WHERE sub.member = '{context.member}';""", as_dict=True)
     # print(f'\n\n\n\n my class {context.my_class.class_name} {context.my_class.duration} \n\n\n\n')

# see their lockers
def get_my_locker(context):
     context.my_locker = frappe.db.sql(f"""SELECT locker, duration FROM `tabGym Locker Subscription` sub WHERE sub.member = '{context.member}';""", as_dict=True)
     
# see their trainers
def get_my_trainer(context):
     context.my_trainer = frappe.db.sql(f"""SELECT * FROM `tabGym Trainer Subscription` sub WHERE sub.member = '{context.member}';""", as_dict=True)

# see the workout plan subscription
def get_my_workout(context):
     context.my_workout = frappe.db.sql(f"""SELECT * FROM `tabGym Workout Plan Subscription` sub WHERE sub.member = '{context.member}';""", as_dict=True)

def get_membership(context):
     # membership_info = frappe.get_value("Gym Membership", {"member": context.member})
     context.mem_ship_info = frappe.db.sql(f"SELECT ship.member, mem.full_name, ship.from, ship.to FROM `tabGym Membership` ship LEFT JOIN `tabGym Member` mem ON ship.member = mem.name WHERE ship.member = '{context.member}';", as_dict=True)



     return context


@frappe.whitelist(allow_guest=True)
def book_class():
  frappe.msgprint("call me")
  return [{'class':'Eshetie'}]

@frappe.whitelist()
def test_method():
    frappe.msgprint('Hai I am Here')
    