import openpyxl
import pprint

wb = openpyxl.load_workbook('vocab.xlsx')
sheet = wb['Sheet1']
sheet
sheet_new = wb.create_sheet('Sheet_new')
wb.save('vocab.xlsx')
