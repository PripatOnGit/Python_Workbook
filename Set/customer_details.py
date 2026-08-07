from collections import defaultdict


orders = [
    {"id": "O1", "customer": "Alice", "amount": 320, "status": "delivered"},
    {"id": "O2", "customer": "Bob",   "amount": 80,  "status": "pending"},
    {"id": "O3", "customer": "Alice", "amount": 150, "status": "delivered"},
    {"id": "O4", "customer": "Carol", "amount": 210, "status": "cancelled"},
    {"id": "O5", "customer": "Bob",   "amount": 90,  "status": "delivered"},
    {"id": "O6", "customer": "Carol", "amount": 340, "status": "delivered"},
]

#1.A set of customers who have at least one delivered order
order_delivered_set = {o['customer'] for o in orders if o['status']=='delivered'}
print(order_delivered_set)

#2.A dict of {customer: total_amount} for delivered orders only
totals = defaultdict(int)
for o in orders:
    if o['status'] == 'delivered':
        totals[o['customer']] += o['amount']
print(f"customers with total ampunt: {totals}")

#3.A list of order IDs where amount > 200, sorted highest to lowest
sorted_orders = sorted([o for o in orders if o['amount'] > 200], 
                        key=lambda x: x['amount'], reverse=True)
order_ids = [o['id'] for o in sorted_orders]
print(f"ordered list: {order_ids}")

#4.A tuple of the customer with the highest total delivered amount and their total —("Name", total)
#print(max(totals, key=lambda x: totals[x]))

top_customer = max(totals, key=lambda x: totals[x])
result  = top_customer,totals[top_customer]
print(f"top customer: {result}")