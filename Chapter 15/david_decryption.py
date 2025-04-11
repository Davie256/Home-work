# Write your code here :-)
import os, sys, PyPDF2

def decrypt_pdf(input_path, password):
    try:
        with open(input_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            if not reader.is_encrypted:
                print(f"Skipping unencrypted file: {input_path}")
                return

            if not reader.decrypt(password):
                print(f"Incorrect password for: {input_path}")
                return

            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)

            output_path = input_path.replace('.pdf', '_decrypted.pdf')
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

            print(f"Decrypted: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main(folder_path, password):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith('.pdf') and '_decrypted.pdf' not in filename:
                full_path = os.path.join(foldername, filename)

                try:
                    reader = PyPDF2.PdfReader(full_path)
                    if reader.is_encrypted:
                        decrypt_pdf(full_path, password)
                except Exception as e:
                    print(f"Skipping file due to error: {full_path}")


if len(sys.argv) != 3:
    print("Usage: python decrypt_pdfs.py <folder_path> <password>")
    sys.exit(1)

folder_path = sys.argv[1]
password = sys.argv[2]

#folder_path = 'C:\\Users\\david'
#password = 'woods'

main(folder_path, password)
