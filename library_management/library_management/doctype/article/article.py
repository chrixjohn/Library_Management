# Copyright (c) 2025, Faris Ansari and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Article(WebsiteGenerator):
     pass

def article_hook(doc, method):
        frappe.msgprint(f"{method} triggered for Article: {doc.article_name}")
        if doc.status == "Issued":
               frappe.msgprint("This article is marked as Issued.")     
