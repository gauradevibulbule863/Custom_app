# Copyright (c) 2024, Indictrans and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import re
import datetime
from datetime import datetime
from frappe.utils import validate_email_address, validate_phone_number
from frappe.utils import today, getdate
from frappe.model.document import Document



class ServerSideScripting(Document):
	def validate(self):
		
		# self.calculates_age()
		self.validate_mobile_number()
		self.validate_email()
		self.validate_dob()
		# self. validate_mobile_number()
		self.set_full_name()
		self.validate_unique_relations()
		
		
	
	def validate_name_field(self,value):
		
		
		if not value:
			return ""
		value = value.strip()
		capitalized_value = value.capitalize()
		
		if not re.match(r'^[A-Z][a-zA-Z]*$',capitalized_value):
				frappe.throw(_("name must start with a capital letter and contain only alphabets."))
		return capitalized_value

		
	
	def set_full_name(self):
		first_name = self.validate_name_field(self.first_name) if self.first_name else ''
		middle_name = self.validate_name_field(self.middle_name) if self.middle_name else ''
		last_name = self.validate_name_field(self.last_name) if self.last_name else ''
		
		full_name = " ".join(filter(None, [first_name, middle_name, last_name])).strip()
		self.full_name = full_name

	def validate_unique_relations(self):
		
		# father_mother_set = set()
		# other_relation_set = {}

		# for row in self.family_members:
		# 	relation = row.relation
		# 	name = row.name1
		# 	if relation in ["father","mother"]:
		# 		if relation not in father_mother_set:
		# 			father_mother_set.add(relation)
		# 		else:
		# 			frappe.throw(_("Duplicate entries found for relation '{0}'. Each 'Father' and 'Mother' entry must be unique.".format(relation)))
		# 	else:
		# 		if relation not in other_relation_set:
		# 			other_relation_set.add(name,relation)
		# 		else:
		# 			 frappe.throw(_("Duplicate name '{0}' found for relation '{1}'.".format(name, relation)))

		
		pairs = [(row.name1, row.relation)for row in self.family_members]
		unique_pairs = list(set(pairs))
		if len(pairs) != len(unique_pairs):
			frappe.throw(_("Duplicate entries found in family members. Each name and relation pair must be unique."))


				
		
				
			
			
			
		# 	if entry in relations:
				
		# 		frappe.throw("duplicate entries")
		# 	relations.add(entry)
		# 	relations = set(relations)
		# 		frappe.throw(_("Relation '{0}' is repeated in the family members with'{1}' list.".format(member.relation,member.name)))
		# 	else:
		# 		relations.append(member.relation)

		# res = frappe.as_json(self.family_members)
		

		# print(f"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChuild Table Details={res}\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\\n""")

		# print(f"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChuild Table Details:{self.family_members}\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\\n""")
		# for row in self.family_members:
		# 	print(f"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRow Details:{ row.as_dict() }\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\\n""")
		
		# seen_entries = set()

        

	



		
		# f_name = []
		# if self.first_name:
		# 	f_name = self.first_name
		# if self.middle_name:
		# 	f_name =' ' + self.middle_name
		# else:
		# 	self.f_name =""
		# if self.last_name:
		# 	f_name =' ' +  self.last_name
		# else:
		# 	self.f_name = ""

		# self.full_name = f_name.trim()

		# f_name = [self.first_name, self.middle_name, self.last_name]



		# full_name =' '.join(name for  name in f_name if f_name)
		# name = full_name.split()
		# capitalized_text = name.title()


		# self.full_name = capitalized_text
		
	def validate_mobile_number(self):
		validate_phone_number(self.mob_no, throw=True) # InvalidPhoneNumberError
		# if self.mob_no:
		# 	mobile_pattern= re.compile(r"^\d{10}$") 
		
		# 	if not mobile_pattern.match(self.mob_no):
		# 		frappe.throw(_("Mobile no must be exactly 10 digits"))
		
	def validate_date(self):
		input_date = self.dob
		today = datetime.now().date()

		if input_date > today:
			frappe.throw("Date can not be in the future")

	
	def validate_email(self):
		
		if self.email:
			# try:
			validate_email_address(self.email, throw=True)
			# except frappe.ValidationError:
			# 	frappe.throw(_("Please enter a valid email address"))

	def validate_dob(self):
		if self.dob:  
			dob_date = getdate(self.dob)
			current_date = getdate(today())
			
			if dob_date > current_date:
				frappe.throw(_("Date of Birth cannot be in the future. Please select a valid date."))

	def calculates_age(self):
		if self.dob:
			today = datetime.today()
			dob = self.dob
			age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
			self.age = age


	

@frappe.whitelist()
def calculate_age(dob=None):
	if not dob:
		return
	today =datetime.today()
	dob = getdate(dob)
	age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
	return age





















	
	# 	if not self.is_valid_full_name(self.full_name):
	# 		frappe.throw("full name must only contain alphabetic characters, with each word srarting with a capital letter")

	# def is_valid_full_name(self,name):

		
	# 	full_name = name.split()
	# 	pattern = [word for word in full_name if re.match( r'\b[A-Z][a-z]*\b', word)]
		
	# 	return pattern




		
		


		



	# self.get_document()
	# self.new_document()
	# self.save_document()
	# frappe.msgprint("Hello Frappe from validate event")
	# frappe.msgprint(_("Hello My Full Name Is'{0} ").format(self.first_name + " " + self.middle_name + " " + self.last_name))
	
	# for row in self.get("family_members"):
	# 	frappe.msgprint(_(
	# 		"{0}, The Family Member name is '{1}' and relation is '{2}'").format(row.idx,row.name1,row.relation)
	# 	)
	


	# def before_save(self):
	# 	frappe.throw("Hlo, frappe from before_save event")

	# def before_insert(self):
	# 	frappe.throw("Hlo, frappe from before_save event")==

	# def after_insert(self):
	# 	frappe.throw("Hlo, frappe from after_insert event")

	# def on_update(self):
	# 	frappe.throw("Hlo, frappe from on_update event")

	# def before_submit(self):
	# 	frappe.throw("Hlo, frappe from before_submit event")

	# def on_submit(self):
	# 	frappe.throw("Hlo, frappe from on_submit event")

	# def on_cancel(self):
	# 	frappe.throw("Hlo, frappe from on_cancel event")

	# def on_trash(self):
	# 	frappe.throw("Hlo, frappe from on_trash event")
	
	# def after_delete(self):
	# 	frappe.throw("Hlo, frappe from after_delete event")
 

	# def validate(self):
	# 	self.get_document(self)

	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting',self.client_side_doc)
	# 	frappe.msgprint(_("The First Name is {0} and age is {1}").format(doc.first_name, doc.age))

	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
	# 	message = _("The First Name is {0} and age is {1}").format(doc.first_name, doc.age)
	# 	frappe.msgprint(message)


	#def validate(self):
		#self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Jake'
	# 	doc.last_name = 'jay'
	# 	doc.age = 13
	# 	doc.append("family_members",{	"name1":"jain",
	# 						   			"relation":"sister",
	# 						   			"age":14})
	# 	doc.insert()


	# def validate(self):
	# 	self.save_document()

	# def save_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.last_name = 'jay'
	# 	doc.age = 31

	# 	doc.save()
		
		
	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting','PR-0017')

	
	# def validate(self):
	# 	self.delete_document()

	# def delete_document(self):
	# 	doc = frappe.get_doc('client Side Scripting','PR-0012')
	# 	doc.delete()


	# def validate(self):
	# 	self.db_set_document()

	# def db_set_document(self):
	# 	doc = frappe.get_doc('client Side Scripting','PR-0021')
	# 	doc.db.set('age',45)




	

	

	

