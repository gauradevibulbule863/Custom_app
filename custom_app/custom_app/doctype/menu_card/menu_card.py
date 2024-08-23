# Copyright (c) 2024, Indictrans and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class MenuCard(Document):
    def validate(self):
        self.check_for_duplicate_entries()
    
    def before_save(self):

        self.total_amount = self.calculate_total_amount()
    

    def check_for_duplicate_entries(self):
        # Check if there is an existing entry with the same posting_date and hotel_name
        duplicate_entry = frappe.db.exists('Menu Card', {
            'hotel_name': self.hotel_name,
            'posting_date': self.posting_date,
            'docstatus': ('!=', 2),  # Exclude canceled entries
            'name': ('!=', self.name)  # Exclude the current document being validated
        })

        if duplicate_entry:
            frappe.throw(_("A Menu Card for hotel '{0}' already exists on date {1}. Please choose a different date.")
                         .format(self.hotel_name, self.posting_date))


    






    def calculate_total_amount(self):
        total_amount = 0
        for row in self.daily_menu_card:
            total_amount += row.price
        return total_amount 
        