data = [
    {"name": "Alice", "age": "28", "score": "92.5"},
    {"name": "Bob",   "age": "abc", "score": "85"},
    {"name": "Carol", "age": "31",  "score": "invalid"},
    {"name": "Dan",   "age": "25",  "score": "78.5"},
]

'''
Write a function that:

Converts age to int and score to float for each record
If conversion fails — skip that field, keep original string value, print a warning
Returns list of processed records
Uses finally to print "Processing complete" after every record — success or failure
'''

def handle_exception(data):
    record = []
    for item in data:
        try:
            item['age'] = int(item['age'])    
        except ValueError as e:
            print(f"Warning: {e}")
        try:
            item['score'] = float(item['score'])
        except ValueError as e:
            print(f"Warning: {e}")
            
        record.append(item)
        print("Processing complete")

    return record

result = handle_exception(data)
print(result)