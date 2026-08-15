from collections import defaultdict
import csv

def emp(file):
    dept_salaries = defaultdict(list)
    dept_avg_sal = {}
    try:
        with open(file,'r') as f:
            content = csv.DictReader(f)
            for row in content:
                dept = row['department']
                sal = float(row['salary'])
                dept_salaries[dept].append(sal)
    
    except FileNotFoundError as e:
        print(f"File not found. {e}")
        return {} 
    for dept,sal in dept_salaries.items():
        dept_avg_sal[dept] = (sum(sal)/len(sal))
    #return {dept: sum(sal)/len(sal) for dept, sal in dept_salaries.items()}
    return dept_avg_sal

print(emp('D:/Priyanka_Vault/Python_Workbook/file_IO/data.csv'))




