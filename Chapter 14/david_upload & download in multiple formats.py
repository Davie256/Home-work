# Write your code here :-)
import ezsheets
import os

# Path to your input file (e.g., CSV or XLSX)
input_file = 'C:\\Users\\david\\mu_code\\example10.xlsx'  # Change to your file

# Upload the spreadsheet to Google Sheets
ss = ezsheets.upload(input_file)
print(f"Uploaded: {ss.title}")

# Output filenames
output_filename = os.path.splitext(os.path.basename(input_file))[0]

# Download in various formats
ss.downloadAsExcel(f'{output_filename}.xlsx')
ss.downloadAsODS(f'{output_filename}.ods')
ss.downloadAsPDF(f'{output_filename}_new.pdf')
ss.downloadAsCSV(f'{output_filename}.csv')
ss.downloadAsTSV(f'{output_filename}.tsv')

print("Downloads complete:")
print(f"- {output_filename}.xlsx")
print(f"- {output_filename}.ods")
print(f"- {output_filename}_new.pdf")
print(f"- {output_filename}.csv")
print(f"- {output_filename}.tsv")
