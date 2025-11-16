frappe.ui.form.on("Formulaire CarGlass", {
    refresh(frm) {

        // --- Ordre de service (PDF) ---
        frm.add_custom_button(__('📄 Ordre de service (PDF)'), () => {
            const format = "Ordre de service";
            const url = frappe.urllib.get_full_url(
                `/api/method/frappe.utils.print_format.download_pdf?doctype=${frm.doctype}&name=${frm.docname}&format=${encodeURIComponent(format)}&no_letterhead=0`
            );
            window.open(url);
        });

    }
});
