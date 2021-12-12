import openpyxl
import pprint

wb = openpyxl.load_workbook('vocab.xlsx')
sheet = wb['Sheet1']


wb.save('vocab.xlsx')
