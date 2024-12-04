import os
from pathlib import Path

def Finding_big_files():

    user_path = input('Enter the folder path with the big files in this format; C:\\...\\....\n')
    required_size = 100*1024*1024
    print('\nThese are the big file required:')

    for folderName, subfolders, filenames in os.walk(user_path):
        for folder in filenames:
            file_path = os.path.join(user_path, file)
            file_size = os.path.getsize(file_path)

            if file_size > required_size:
                #print(os.path.join(folderName, file))
                print(f'\n{file_path}')

Finding_big_files()
