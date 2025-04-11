# Write your code here :-)
import ezsheets

# Connect to the publicly shared spreadsheet
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]  # Get the first sheet

# Start from row 2 because row 1 is the header
for row_num in range(2, sheet.rowCount + 1):
    row = sheet.getRow(row_num)

    # Skip empty or malformed rows
    if len(row) < 3 or not all(row[:3]):
        continue

    try:
        beans_per_jar = int(row[0])
        jars = int(row[1])
        total_beans = int(row[2])

        if beans_per_jar * jars != total_beans:
            print(f"[!] Mismatch found on row {row_num}: {beans_per_jar} x {jars} = {beans_per_jar * jars}, but Total Beans = {total_beans}")
            break  # Stop after finding the first error

    except ValueError:
        print(f"[!] Invalid data on row {row_num}: {row}")
        continue
