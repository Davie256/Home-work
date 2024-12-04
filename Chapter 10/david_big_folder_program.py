# Write your code here :-)
import os
from pathlib import Path

def Finding_file_size():

    user_path = input('Enter the folder path whose size is required; C:\\...\\....\n')

    print('\nThis is the folder size required:')
    total_files_size = 0

    for folderName, subfolders, files in os.walk(user_path):
        for file in files:
            file_path = os.path.join(user_path, file)
            file_size = os.path.getsize(file_path)

            total_files_size += file_size

    print(f'Folder size : {total_files_size} bytes')

Finding_file_size()
