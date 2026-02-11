// Copyright (c) 2025, SARL MYNDALL and contributors
// For license information, please see license.txt

frappe.ui.form.on("RSA Demande", {

	 after_workflow_action(frm) {
        if (frm.doc.workflow_state === "SVC Fait") {
            frappe.set_route('Form', 'RSA Fiche Intervention', 'new', {
                dossier_rsa: frm.doc.name
            });
        }
    },


	ref: function(frm) {
        // Clear the num_de_police field first
        frm.set_value('num_de_police', null);

        if (frm.doc.ref) {
            // Look for the record in Police Auto Data
            frappe.db.get_value('Police Auto Data', { name: frm.doc.ref }, 'parent')
            .then(r => {
                if (r.message && r.message.parent) {
                    // Set num_de_police to the parent value
                    frm.set_value('num_de_police', r.message.parent);
                }
            });
        }
    },


    refresh(frm) {

		 frm.add_custom_button("Select Prestataire", () => {
            let d = new frappe.ui.Dialog({
                title: "Select Prestataire",
                size: "extra-large",
                fields: [
                    {
                        fieldname: "prestataire_table",
                        fieldtype: "Table",
                        cannot_add_rows: true,
                        in_place_edit: false,
                        fields: [
                        // Added in_list_view: 1 to make columns visible
                        { fieldname: "nom", label: "Name", fieldtype: "Data", read_only: 1, in_list_view: 1 },
                        { fieldname: "numero_1", label: "Num1", fieldtype: "Data", read_only: 1, in_list_view: 1 },
                        { fieldname: "numero_2", label: "Num2", fieldtype: "Data", read_only: 1, in_list_view: 1 },
                        { fieldname: "numero_chauffeur", label: "Chauffeur", fieldtype: "Data", read_only: 1, in_list_view: 1 },
                        { fieldname: "wilaya", label: "Wilaya", fieldtype: "Data", read_only: 1, in_list_view: 1 },
                        { fieldname: "commune", label: "Commune", fieldtype: "Data", read_only: 1, in_list_view: 1 }
                    ]
                    }
                ],
                primary_action_label: "Select",
                primary_action() {
                    let row = d.fields_dict.prestataire_table.grid.get_selected_children()[0];
                    if (row) {
                        frm.set_value("prestataire", row.name);
                        d.hide();
                    }
                }
            });

             frappe.db.get_list("Prestataire", {
                fields: ["name","nom", "numero_1", "numero_2", "numero_chauffeur", "wilaya", "commune"],
				 filters: {
                    wilaya: frm.doc.lieu_du_sinistre,
                    type: "RSA"
                },
                limit: 50
            }).then(data => {
                d.fields_dict.prestataire_table.df.data = data;
                d.fields_dict.prestataire_table.refresh();
            });

            d.show();
        });



        if (frm.is_new()) return;

        // frm.clear_custom_buttons();
        // frm.page.actions.hide();

        get_workflow_state_colors(frm).then(state_colors => {

            frappe.call({
                method: "frappe.model.workflow.get_transitions",
                args: { doc: frm.doc },
                callback(r) {
                    if (!r.message) return;

                    const btn_class =
                        state_colors[frm.doc.workflow_state] || "btn-primary";

                    r.message.forEach(t => {
                        frm.add_custom_button(
                            __(t.action),
                            () => apply_workflow(frm, t.action)
                        ).addClass(btn_class);
                    });
                }
            });

        });


    }
});

function apply_workflow(frm, action) {
    frappe.call({
        method: "frappe.model.workflow.apply_workflow",
        args: { doc: frm.doc, action },
        callback() {
            frm.reload_doc();
        }
    });
}


function workflow_btn_class(action) {
    const a = action.toLowerCase();

    if (a.includes("approve")) return "btn-success";
    if (a.includes("reject"))  return "btn-danger";
    if (a.includes("cancel"))  return "btn-warning";
    if (a.includes("submit"))  return "btn-primary";

    return "btn-secondary";
}


function apply_workflow(frm, action) {
    frappe.call({
        method: "frappe.model.workflow.apply_workflow",
        args: {
            doc: frm.doc,
            action: action
        },
        callback() {
            frm.reload_doc();
        }
    });
}

function get_workflow_state_colors() {
    return new Promise(resolve => {

        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Workflow State",
                fields: ["workflow_state_name", "style"],
                limit_page_length: 100
            },
            callback(r) {
                const map = {};

                (r.message || []).forEach(ws => {
                    map[ws.workflow_state_name] = style_to_btn_class(ws.style);
                });

                resolve(map);
            }
        });

    });
}


function style_to_btn_class(style) {
    const styles = {
        "Success": "btn-success",
        "Warning": "btn-warning",
        "Danger": "btn-danger",
        "Primary": "btn-primary",
        "Secondary": "btn-secondary",
        "Info": "btn-info"
    };
    return styles[style] || "btn-primary";
}

