#!/usr/bin/python3

from openpyxl import load_workbook
from collections import Counter

class FileOperations:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_file(self):
        sheet = None
        try:
            workbook = load_workbook(filename=self.file_path)
            sheet = workbook.active
        except:
            print("An exception occurred while loading file.")
        return sheet

    def read_data(self, str_to_search_for, sheet):
        lectures = []
        try:
            for i in range(2, sheet.max_row, 1): #from 2 because data starts from row 2
                if str_to_search_for in sheet.cell(row=i, column=2).value:
                    lectures.append(sheet.cell(row=i, column=2).value)
        except:
            print("An exception occurred while reading data.")
        return lectures   
        
    

    