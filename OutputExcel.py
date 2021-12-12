import openpyxl
import pprint

wb = openpyxl.load_workbook('vocab.xlsx')
sheet = wb['Sheet1']
sheet.append(["new", "mới"])
sheet_new = wb.create_sheet('Sheet_new')
wb.save('vocab.xlsx')
