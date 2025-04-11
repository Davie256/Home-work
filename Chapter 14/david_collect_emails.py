# Write your code here :-)
import ezsheets

# Load all spreadsheets (will prompt you the first time)
ss = ezsheets.Spreadsheet('david')  # Or use your actual spreadsheet name
sheet = ss[0]  # First sheet in the spreadsheet

# Skip the header row and collect emails
emails = []
for row in sheet.getRows()[1:]:
    if len(row) > 1:  # Make sure the row has at least two columns
        email = row[1].strip()
        if email:
            emails.append(email)

# Output the collected emails
print("Collected Email Addresses:")
for e in emails:
    print(e)
