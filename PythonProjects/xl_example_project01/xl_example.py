import openpyxl as xl
from pathlib import Path

path = Path(r'C:\Users\Vinayak Ganesh\Projects\PythonProjects\Python_projects\xl_example_project01\transactions.xlsx')
wb = xl.load_workbook(path)
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(2, 1)
print(cell.value)
