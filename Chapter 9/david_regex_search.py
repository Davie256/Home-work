import os
import re

def search_files(folder_path, regex):

    if not os.path.exists(folder_path):
        print('Folder path does not exist.')
        return

    pattern = re.compile(regex)

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            print(f'Searching in "{filename}":.....')

            with open(file_path, 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    if re.search(pattern, line):
                        print(f' Line {line_number}: {line.strip()}')

def user_content():
    folder_path = input('Enter the folder path: \n')
    regex = input('Enter the regular expression to search: \n')
    search_files(folder_path, regex)

user_content()

