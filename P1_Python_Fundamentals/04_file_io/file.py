from collections import defaultdict

def file_ops(file):
    counts = defaultdict(int)
    try:
        with open (file, 'r') as f:
            for line in f:
                level = line.split(':',1)[0].strip()
                counts[level] += 1          
    except FileNotFoundError as e:
        print(f"File Not found: {e}")
    finally:
        print("Processed attempted")
    return dict(counts)

print(file_ops('D:/Priyanka_Vault/Python_Workbook/file_IO/server_logs.txt'))
