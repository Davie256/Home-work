# Write your code here :-)
import openpyxl
import os

def finding_txt_files():

    file_names = []
    folder_path = 'C:\\Users\\david\\waaa'

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            file_names.append(file_path)
    return file_names

def read_text_files():

    contents = []

    file_names = finding_txt_files()

    for file_name in file_names:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            contents.append([line.strip() for line in lines])
    return contents

def write_to_spreadsheet(output_file):

    contents = read_text_files()

    wb = openpyxl.Workbook()
    sheet = wb.active

    for col_index, file_content in enumerate(contents, start=1):
        for row_index, line in enumerate(file_content, start=1):
            sheet.cell(row=row_index, column=col_index, value=line)

    wb.save(output_file)

def main():

    output_file = 'C:\\Users\\david\\new1.xlsx'

    write_to_spreadsheet(output_file)

main()
