# Write your code here :-)
import sys
import openpyxl

def blankRowInserter(N,M):
    wb = openpyxl.load_workbook('C://Users//david//multiplication_table 7.xlsx')
    sheet = wb.active

    insert_position = N
    num_row_to_insert = M

    sheet.insert_rows(insert_position, num_row_to_insert)

    wb.save(f'C://Users//david//{N} {M} myProduce.xlsx')
    print(f'blankRowInserter program is saved as "{N} {M} myProduce.xlsx".')

def main():
    if len(sys.argv) != 3:
        print('The number of arguments are less than the required')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        M = int(sys.argv[2])

        if N <= 0 or M <= 0:
            print('Pliz provide positive integers')
            sys.exit(1)
        blankRowInserter(N,M)

    except ValueError():
        print('Please provide a valid integers.')
        sys.exit(1)

main()
