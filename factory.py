# this code demonstrates the working of the system with at least three test cases for each system aspect

from administrator import Administrator
from customer import Customer

# Initialize Admin
admin = Administrator(admin_id=1)

# --- Create Customers ---
cust1 = Customer(cust_id=101, name="Alice", address="123 Main St")
cust2 = Customer(cust_id=102, name="Bob", address="456 Oak Ave")
cust3 = Customer(cust_id=103, name="Charlie", address="789 Pine Blvd")

admin.add_customer(cust1)
admin.add_customer(cust2)
admin.add_customer(cust3)

# --- Place Orders ---
order1 = cust1.place_order({"item": "Laptop", "price": 999})
order2 = cust2.place_order({"item": "Tablet", "price": 499})
order3 = cust3.place_order({"item": "Monitor", "price": 299})
order4 = cust1.place_order({"item": "Mouse", "price": 49})
order5 = cust2.place_order({"item": "Keyboard", "price": 89})

admin.add_order(order1)
admin.add_order(order2)
admin.add_order(order3)
admin.add_order(order4)
admin.add_order(order5)

# --- Mark Orders Delivered ---
order1.mark_delivered()
order2.mark_delivered()
order3.mark_delivered()

# --- File Complaints ---
cust1.file_complaint(order_id=order1.order_id, reason="Battery issue")
cust2.file_complaint(order_id=order2.order_id, reason="Damaged on arrival")
cust3.file_complaint(order_id=order3.order_id, reason="Dead pixels")

# --- Initiate Returns ---
cust1.initiate_return(order_id=order1.order_id, reason="Wrong model")
cust2.initiate_return(order_id=order2.order_id, reason="Doesn't match description")
cust3.initiate_return(order_id=order3.order_id, reason="Too large")

# --- Receive Gifts (Customer-triggered) ---
cust1.receive_gift("Free USB Drive")
cust2.receive_gift("Welcome Gift Box")
cust3.receive_gift("Promo Voucher")

# --- Admin Logs Custom Events ---
admin.log_custom_event("Anniversary Offer", customer_id=101, metadata={"value": "$50 off"})
admin.log_custom_event("Loyalty Reward", customer_id=102, metadata={"points": 300})
admin.log_custom_event("Referral Bonus", customer_id=103, metadata={"bonus": "10% discount"})

# --- Dashboard Summary ---
print("\n--- Dashboard Metrics ---")
print(admin.get_dashboard_metrics())

# --- View Customer Event Histories ---
for cust in [cust1, cust2, cust3]:
    print(f"\n--- Event History for {cust.name} ---")
    for event in admin.view_customer_events(cust.cust_id):
        print(" -", event.get_summary())