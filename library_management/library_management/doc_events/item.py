import frappe

def validate_item(doc, method):
    # Example validation logic
    if not doc.item_name:
        frappe.throw("Item Name is required!")
    

    if doc.stock_uom != "Nos":
        frappe.msgprint("Warning: Stock UOM is not 'Nos' chris")
