import frappe
from frappe import utils


def execute():
     membership = frappe.get_all("Gym Membership", fields=["member", "from", "to"])

     for ship in membership: 
          to = convert_date(ship.to)
          to_day = utils.today()
          
          if to < to_day:
               frappe.db.set_value("Gym Membership", ship.name, "status", "Expired", update_modified=False)
          else:
               frappe.db.set_value("Gym Membership", ship.name, "status", "Active", update_modified=False)


def convert_date(date): 
    return date.strftime("%Y-%m-%d")


     