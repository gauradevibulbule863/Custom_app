// Copyright (c) 2024, Indictrans and contributors
// For license information, please see license.txt





frappe.ui.form.on('Menu Card', {

    onload: function (frm) {
		frm.set_query("hotel_name", function () {
			return {
				filters: {
					is_active: 1,
					
				},
			};
		});
	},

    // // Trigger when form is loaded or child table is refreshed
    // refresh: function(frm) {
    //     calculate_total_amount(frm);
    // },

    // // Trigger whenever a row in the child table is modified
    // 'daily_menu_card_table': function(frm, cdt, cdn) {
    //     calculate_total_amount(frm);
    // },

    // // Trigger on any change in the child table
    // 'daily_menu_card_table_remove': function(frm) {
    //     calculate_total_amount(frm);
    // }
});

// Function to calculate the total amount
// function calculate_total_amount(frm) {
//     let total = 0;

//     // Loop through each row in the child table
//     frm.doc.daily_menu_card.forEach(function(row) {
//         total += row.Price;
//     });

//     // Set the total amount in the parent Doctype
//     frm.set_value('total_amount', total);
// }




// frappe.ui.form.on('Menu Card', {
//     onload: function (frm) {
//         frm.fields_dict['hotel_name'].get_query = function () {
//             return {
//                 filters: {
//                     'is_active': 1  
//                 }
//             };
//         };
//     }
// });

