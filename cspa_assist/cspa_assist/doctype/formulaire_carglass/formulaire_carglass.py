# Copyright (c) 2025, SARL MYNDALL and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class FormulaireCarGlass(Document):
	def on_submit(self):

		# --- STEP 1: Ensure Police Assurance Auto exists ---
		if not self.num_de_police:
			frappe.throw("Le champ <b>Numéro de police</b> est obligatoire.")

		existing_policy = frappe.db.exists(
			"Police Assurance Auto",
			{"numero_de_police": self.num_de_police}
		)

		if not existing_policy:
			policy = frappe.get_doc({
				"doctype": "Police Assurance Auto",
				"compagnie_dassurance": self.compagnie_dassurance,
				"numero_de_police": self.num_de_police,
				"date_debut": self.date_deffet,
				"date_echance": self.date_déchéance,
				"table_daub": [
					{
						"marque": self.marque,
						"immatriculation": self.immatriculation,
						"num_chassis": "",
						"modele": self.modèle,
						"couleur": self.couleur,
					}
				]
			})
			policy.insert(ignore_permissions=True)
			existing_policy = policy.name

		# --- STEP 2: Create Demande CarGlass (copy required fields) ---
		demande = frappe.get_doc({
			"doctype": "Demande Car Glass",
			"num_identité_national": self.num_identité_national,
			"prenom": self.prenom,
			"nom": self.nom,
			"numero": self.numero,
			"email": self.email,
			"num_de_police": self.num_de_police,
			"img_contrat": self.img_contrat,
			"img_permis": self.img_permis,
			"img_carte_grise": self.img_carte_grise,
			"compagnie_dassurance": self.compagnie_dassurance,
			"police_assurance": existing_policy  # link to Police Assurance
		})
		demande.insert(ignore_permissions=True)

		# --- STEP 3: Redirect user to Demande CarGlass ---
		frappe.local.response["type"] = "redirect"
		frappe.local.response["location"] = f"/app/demande-car-glass/{demande.name}"


