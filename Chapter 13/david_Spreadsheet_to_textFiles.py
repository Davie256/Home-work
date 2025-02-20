# Write your code here :-)
import openpyxl

wb = openpyxl.load_workbook('C://Users//david//new1.xlsx')
sheet = wb.active

for col_index, column in enumerate(sheet.iter_cols(values_only=True), start=1):

    output_file = f'C://Users//david//waaa//column_{col_index}.txt'

    with open(output_file, 'w') as file:
        for cell_value in column:
            if cell_value is not None:
                file.write(str(cell_value) + ' ')

    print(f'Column {col_index} written to {output_file}')
