import openpyxl
import random


class Flashcard:
    def __init__(self):
        self.word = ''
        self.meaning = ''
        self.choose_a_row()

    def choose_a_row(self):
        wb = openpyxl.load_workbook('vocab.xlsx')
        sheet = wb['Sheet1']
        i = random.randint(2, sheet.max_row+1)
        row1 = sheet[i]
        current_row = []
        for cell in row1:
            current_row.append(cell.value.replace("\n", ""))
        self.word = current_row[0]
        self.meaning = current_row[1]
