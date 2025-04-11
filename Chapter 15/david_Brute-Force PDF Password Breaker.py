# Write your code here :-)
import PyPDF2

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def try_decrypt(pdf_path, dictionary):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        if not reader.is_encrypted:
            print("The PDF is not encrypted.")
            return

        for word in dictionary:
            for attempt in (word.lower(), word.upper()):
                result = reader.decrypt(attempt)
                if result:
                    print(f'Password found: {attempt}')
                    return attempt
                else:
                    print(f'Tried: {attempt}')
                    return attempt

        print('[X] Password not found.')
        return None

pdf_file = 'C:\\Users\\david\\encryptedminutes_decrypted.pdf'
dict_file = 'C:\\Users\\david\\Automate\\aaa\\dictionary.txt'

words = load_dictionary(dict_file)

try_decrypt(pdf_file, words)
