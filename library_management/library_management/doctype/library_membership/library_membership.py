# Copyright (c) 2025, Faris Ansari and contributors
# For license information, please see license.txt

from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

import frappe


class LibraryMembership(Document):
    # check before submitting this document
    def before_submit(self):
        pass
        # exists = frappe.db.exists(
        #     "Library Membership",
        #     {
        #         "library_member": self.library_member,
        #         "docstatus": DocStatus.submitted(),
        #         # check if the membership's end date is later than this membership's start date
        #         "to_date": (">", self.from_date),
        #     },
        # )
        # if exists:
        #     frappe.throw("There is an active membership for this member")

        # # get loan period and compute to_date by adding loan_period to from_date
        # loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
        # self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)

 
