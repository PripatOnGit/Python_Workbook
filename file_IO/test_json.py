
import json
def json_file_handling(file):
    data = {}
    try:
        with open(file) as f:
            employees = json.load(f)
            #print(employees)
        active_emp = []
        for emp in employees['employees']:
            if emp['active'] is True:
                active_emp.append(emp)
        data = {emp['name']:emp['salary'] for emp in active_emp}

    except FileNotFoundError as e:
        print(f"File Not found {e}")
    except json.JSONDecodeError as e:
        print(f"JSON file invalid/currupted {e}")
    finally:
        print("processing done!!")

    return data


print(json_file_handling('D:\\Priyanka_Vault\\Python_Workbook\\file_IO\\data.json'))
