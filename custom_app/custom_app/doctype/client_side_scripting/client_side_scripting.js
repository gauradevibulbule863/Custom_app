// Copyright (c) 2024, Indictrans and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {
	
	
	// refresh: function(frm) {
	// 	frappe.msgprint("Hello User Welcome ")
	// 	//frappe.throw("this is an error")

	// },

	//  onload: function(frm){
	// 	frappe.msgprint("Hlo User Welcome from Onload")
	// },

	// validate: function(frm){
	// 	//frappe.throw("hlo, from validate event")
		
	// 	frappe.msgprint("hlo, from validate event")
	// 	frm.doc.age += 2
	// },

	// before_save: function(frm){
	// 	frappe.throw("hlo, from before_save event")
	// },

	// after_save: function(frm){
	// 	frappe.throw("hlo, from after save event")
	// },

	// // enable:function(frm){
	// // 	frappe.msgprint("hlo, from 'enable' fielname event")
	// // },

	// // age: function(frm){
	// // 	frappe.msgprint("hlo, fom 'age' fieldname event")
	// // },

	// family_members_on_form_rendered: function(frm){
	// 	frappe.msgprint("hlo, 'family_members' table rendered event ")
	// },

	// before_submit: function(frm){
	// 	frappe.throw("hlo, from before_submit event")
	// },

	// after_submit:function(frm){
	// 	frappe.throw("hlo, from after submit event")
	// },

	// before_cancel:function(frm){
	// 	frappe.throw("hlo, from before cancel event")
	// },

	// after_cancel:function(frm){
	// 	frappe.throw("hlo, from after cancel event")
	// },


	// after_save: function(frm){
	// 	frappe.msgprint(_("The Full Name is'{0}'",[frm.doc.first_name + " " + frm.doc.middle_name + " " +frm.doc.last_name]))
		
	// 	for (let row of frm.doc.family_mambers){
	// 		frappe.msgprint(_("{0}.The family member name is'{1}'& relation is '{2}'",[row.idx, row.name1,row.relation]))
	// 	}
	//  },


	// validate:function(frm){
	// 	frm.set_value('full_name',frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name)

	// 	let row = frm.add_child('family_members',{
	// 		name1 : "johnson",
	// 		relation : "father",
	// 		age : 56
	// 	})
	// },

	// refresh:function(frm){
	// 	//frm.set_intro("now u can create new client side scripting doctype")
	// 	if(frm.is_new()){
	// 		frm.set_intro("now u can create new client side scripting doctype")
	// 	}
	// }

	





});


frappe.ui.form.on('Family Members',{
	name1:function(frm){
	frappe.msgprint("hlo, from child doctype 'name' event")
	},

	age(frm, cdt, cdn) {
		frappe.msgprint("hlo, from child doctype 'age' event")
	}
});
