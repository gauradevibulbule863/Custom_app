// Copyright (c) 2024, Indictrans and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server Side Scripting', {
	// refresh: function(frm) {

	// }
	// validate:function(frm){
	// 	full_name(frm)

	// },
	dob: function(frm) {
        if (frm.doc.dob) {
            frappe.call({
                method: 'custom_app.custom_app.doctype.server_side_scripting.server_side_scripting.calculate_age',
                args: {
                    'dob': frm.doc.dob
                },
                callback: function(r) {
					console.log(r)
                    frm.set_value('age', r.message);
                }
            });
        } else {
            frm.set_value('age', 0);
        }
    }






	
	
});

function full_name(frm){
	let name = [];
	if(frm.doc.first_name){
		name.push(frm.doc.first_name)
	}
	if(frm.doc.middle_name){
		name.push(frm.doc.middle_name)
	}
	if(frm.doc.last_name){
		name.push(frm.doc.last_name)
	}
	frm.set_value('full_name',name.join(' '));
}
	




	

