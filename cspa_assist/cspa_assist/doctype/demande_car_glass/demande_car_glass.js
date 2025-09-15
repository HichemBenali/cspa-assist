// Copyright (c) 2025, SARL MYNDALL and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Demande Car Glass", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('Demande Car Glass', {
    refresh: function(frm) {
        frm.fields_dict['immatriculation'].get_query = function(doc) {
            return {
                filters: {
                    parent: doc.num_de_police
                }
            };
        };
    }
});
