# Copyright (c) 2025, Faris Ansari and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re


class LibraryMember(Document):
	# pass
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
		

	def validate(self):
        # Validate email format
		if self.email_address and not frappe.utils.validate_email_address(self.email_address):
			frappe.throw("Invalid email format")

        # Validate phone number (e.g. must be 10 digits)
		if self.phone and not re.fullmatch(r"\d{10}", self.phone):
			frappe.throw("Phone number must be exactly 10 digits")

