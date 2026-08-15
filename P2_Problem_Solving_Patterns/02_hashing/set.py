last_month  = ["C001", "C002", "C003", "C004", "C005"]
this_month  = ["C002", "C003", "C005", "C006", "C007"]


last_month_set = set(last_month)
this_month_set = set(this_month)

print(f"Retained': {last_month_set & this_month_set}")
print(f"Churned: {last_month_set - this_month_set}")
print(f"new: {this_month_set - last_month_set}")