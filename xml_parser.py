import pandas as pd
import xml.etree.ElementTree as ET
import os

input_folder = 'xml_files' 
output_file = 'work_hours_report.xlsx'

all_rows = []

if not os.path.exists(input_folder):
    print(f"Папка {input_folder} не найдена!")
else:
    for filename in os.listdir(input_folder):
        if filename.endswith(".xml"):
            path = os.path.join(input_folder, filename)
            tree = ET.parse(path)
            root = tree.getroot()

            header = root.find('header')
            f_id = header.findtext('facilityId')
            state = header.findtext('stateCode')

            hire_dates = {}
            for emp in root.findall('.//employee'):
                emp_id = emp.findtext('employeeId')
                h_date = emp.findtext('hireDate')
                hire_dates[emp_id] = h_date

            for staff_hours in root.findall('.//staffHours'):
                emp_id = staff_hours.findtext('employeeId')
                
                for work_day in staff_hours.findall('.//workDay'):
                    work_date = work_day.findtext('date')
                    
                    for entry in work_day.findall('.//hourEntry'):
                        row = {
                            'FacilityID': f_id,
                            'State': state,
                            'EmployeeID': emp_id,
                            'HireDate': hire_dates.get(emp_id, ''),
                            'WorkDate': work_date,
                            'Hours': entry.findtext('hours'),
                            'JobTitleCode': entry.findtext('jobTitleCode'),
                            'PayTypeCode': entry.findtext('payTypeCode'),
                            'FileName': filename
                        }
                        all_rows.append(row)

    if all_rows:
        df = pd.DataFrame(all_rows)
        df['Hours'] = pd.to_numeric(df['Hours'], errors='coerce')
        
        df.to_excel(output_file, index=False)
        print(f"Готово! Таблица сохранена в {output_file}. Всего записей: {len(df)}")
    else:
        print("Данные не найдены.")
