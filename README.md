# healthcare-xml-etl-processor
Python script for automated ETL processing of nested XML healthcare staffing and therapy hour reports into structured Excel formats
This project is a specialized ETL (Extract, Transform, Load) pipeline designed to automate the processing of complex, nested XML files used in the US healthcare industry (CMS PBJ reporting). The script parses staffing and therapy hour data, maps employee information, and generates structured Excel reports for compliance auditing.

By replacing manual data entry with this automated solution, the process ensures 100% data integrity and significantly reduces the time required for financial and operational reporting.

🚀 Key Features
Nested XML Parsing: Efficiently navigates complex XML structures to extract deeply nested elements like staffHours, workDay, and hourEntry.

Dynamic Data Mapping: Creates a memory-efficient mapping of employee metadata (e.g., hire dates) and joins it with daily work records.

Data Cleaning & Validation: Utilizes pandas for robust data type conversion (e.g., numeric validation for work hours) to ensure report accuracy.

Batch Processing: Automatically scans entire directories for .xml files and consolidates data into a single, analysis-ready Excel workbook.
