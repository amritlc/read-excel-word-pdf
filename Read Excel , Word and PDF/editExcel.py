import openpyxl
wb = openpyxl.Workbook()
print(wb)

print(wb.get_sheet_names())


sheet = wb.get_sheet_by_name('Sheet')

print(sheet)

sheet['A1'].value
A1 = sheet['A1'].value == None
print(A1)

sheet['A1'] = 13
sheet['A2'] = 'Deadpool'

import os

wb.save('example1.xlsx')
sheet2 = wb.create_sheet()
names = wb.get_sheet_names()
print(names)
print(sheet2.title)
'Sheet1'

sheet2.title = 'New Sheet'
print(wb.get_sheet_names())

wb.save('example3.xlsx')
 
