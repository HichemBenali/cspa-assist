// Copyright (c) 2025, SARL MYNDALL and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Fiche Intervention CarGlass", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('Fiche Intervention CarGlass', {
    refresh(frm) {
        // --- Fiche Intervention (PDF) ---
        frm.add_custom_button(__('🧾 Fiche Intervention (PDF)'), () => {
            const format = "Fiche Intervention";
            const url = frappe.urllib.get_full_url(
                `/api/method/frappe.utils.print_format.download_pdf?doctype=${frm.doctype}&name=${frm.docname}&format=${encodeURIComponent(format)}&no_letterhead=0`
            );
            window.open(url);
        });

        // --- PV Expert (PDF) ---
        frm.add_custom_button(__('📋 PV Expert (PDF)'), () => {
            const format = "PV Expert";
            const url = frappe.urllib.get_full_url(
                `/api/method/frappe.utils.print_format.download_pdf?doctype=${frm.doctype}&name=${frm.docname}&format=${encodeURIComponent(format)}&no_letterhead=0`
            );
            window.open(url);
        });
    }
});
