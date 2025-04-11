# Write your code here :-)
import os, sys, PyPDF2

def encrypt_pdf(input_path, password):
    try:
        with open(input_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                print(f"Skipping already encrypted file: {input_path}")
                return

            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)

            output_path = input_path.replace('.pdf', '_encrypted.pdf')

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        with open(output_path, 'rb') as check_file:
            check_reader = PyPDF2.PdfReader(check_file)
            if not check_reader.is_encrypted:
                print(f"Failed to encrypt: {input_path}")
                return

            try:
                check_reader.decrypt(password)
                first_page = check_reader.pages[0]
                os.remove(input_path)
                print(f"Encrypted and removed: {input_path}")

            except Exception as e:
                print(f"Decryption check failed for: {output_path} - {e}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main(folder_path, password):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith('.pdf') and '_encrypted.pdf' not in filename:
                full_path = os.path.join(foldername, filename)
                encrypt_pdf(full_path, password)

if len(sys.argv) != 3:
    print("Usage: python encrypt_pdfs.py <folder_path> <password>")
    sys.exit(1)

folder_path = sys.argv[1]
password = sys.argv[2]

#folder_path = 'C:\\Users\\david'
#password = 'woods'

main(folder_path, password)

